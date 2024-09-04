from django.shortcuts import render, get_object_or_404,redirect
from .models import Post, User,Profile
from .forms import SignupForm,LoginForm,ProfileForm
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def base(request):
    return render (request, 'base.html')

def posts(request):
    info = Post.objects.all()
    pic = Post.objects.get(id=2)
    uefa = Post.objects.get(id=3)
   
    context = {
        'info':info,
        'uefa':uefa,
        'pic' : pic,
    
    }
    return render(request, 'posts.html', context)

def read(request, id):
    add = get_object_or_404(Post, id=id)
    add.views+=1
    add.save()
    context = {
        'add': add
    }
    return render (request, 'redirect.html', context)
@login_required
def create_post(request):
    if request.method =='POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        user = request.user
        new_post = Post(user=user, title=title, content=content)
        new_post.save()
        context = {
            'success': 'Post Created Successfully!',
            'new_post': new_post
        }
        return render(request, 'creating_post.html', context)
    else:
        context = {}
        return render(request, 'creating_post.html',context)
    
def sign_up(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('posts')

        else:
            form= SignupForm()
            context = {
            'form':form
            }
            return render(request, 'signup.html', context)


    else:
        form= SignupForm()
        context = {
            'form':form
        }
        return render(request, 'signup.html', context)


    
def log_in(request):
    if request.method=='POST':
        form= LoginForm(request, data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user = authenticate(request, username=username,password=password)
            if user != None:
                login(request, user)
                return redirect('posts')
            else:
                form.add_error(None, 'Invalid Username or Password')
                

    else:
        form=LoginForm()
    
    return render(request, 'login.html', {'form':form})
@login_required
def log_out(request):
    logout(request)
    return redirect('posts')
@login_required
def profile(request):
    if not hasattr(request.user, 'profile'):
        x=hasattr(request.user, 'profile')
        print(x)
        Profile.objects.create(user=request.user)

    user_posts= Post.objects.filter(user=request.user)
    if request.method=='POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')

    else:
        form = ProfileForm(instance=request.user)
        context = {
            'form':form,
            'user_posts':user_posts
        }
    return render(request, 'profile.html', context)
