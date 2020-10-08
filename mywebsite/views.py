from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from .forms import UserCreationForm, CommentForm
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def register(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            user_id = form.cleaned_data.get(id)
            print("here goes the user id")
            print(user_id)
            messages.success(request, f'Account created for {username}!')

            return redirect('index')

    return render(request,'mywebsite/register.html',{
        'title': register,
        'form': form
    })

def logoutUser(request):
    logout(request)
    return redirect('index')    


def index(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password= password)

        if user is not None:
            print(username)
            print('***************')
            login(request, user)
            return redirect('dashboard', user.id)
        else:
            messages.warning(request, 'Username or password incorrect..')

    return render(request, 'mywebsite/index.html',{
        'title': 'index'
    })


def courses(request):
    courses = Course.objects.all()
    return render(request, 'mywebsite/courses.html',{
        'title': 'courses',
        'courses': courses
    })

def course_details(request, pk):
    course = Course.objects.get(id=pk)
    section = Section.objects.filter(course=course)
    lessons = Lesson.objects.filter(course=course)
    
    return render(request, 'mywebsite/course_detail.html',{
        'course': course,
        'title': course.title,
        'lessons': lessons,
        'sections': section
    })

def lesson_details(request, pk, pk1):
    course = Course.objects.get(id=pk)
    lesson = Lesson.objects.get(id=pk1)
    section = Section.objects.filter(course=course)
    lessons = Lesson.objects.filter(course=course)

    comments = Comment.objects.filter(lesson=lesson).order_by('id')

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
             content = request.POST.get('body')
             comment = Comment.objects.create(lesson=lesson, user=request.user, body=content)
             comment.save()
    else:
        comment_form = CommentForm()

    return render(request, 'mywebsite/lesson_detail.html',{
        'title': lesson.title,
        'lessons': lessons,
        'sections': section,
        'course': course,
        'current_lesson': lesson,
        'comments': comments,
        'comment_form': comment_form
    })

def dashboard(request, pk):
    profile = Profile.objects.filter(id=pk)
    return render(request, 'mywebsite/dashboard.html',{
        'title': 'dashboard',
        'profile': profile
    })


def blogs(request):
    return render(request, 'mywebsite/blogs.html',{
        'title': 'blogs'
    })

def newsletter(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        email = request.POST.get('email')
        country = request.POST.get('country')

        data = Newsletter(email=email, username=username, country=country)

        data.save()

        messages.success(request, f'Thank you {username} for subscribing, we will contact you soon')
        

    return render(request, 'mywebsite/newsletter.html', {
        'title': 'newletter'
    })

def pricing(request):
    return render(request, 'mywebsite/pricing.html', {
        'title': 'Pricing'
    })

