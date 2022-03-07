from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from datetime import date

def index(request):
    return render(request, 'index.html', {"user": User.objects.all()})

def golf(request):
    if 'user' not in request.session:
        return redirect('/')
    user = User.objects.get(id=request.session['id'])
    context = {
        'user_golf': user.all_golf_by_user.all(),
        'all_golf_by_user': Golf.objects.all(),
    }
    return render(request, 'scotch_dashboard.html', context)

def register(request):
    if request.method == "POST":
        errors = User.objects.basic_validator(request.POST)
        # print(errors)
        if len(errors) != 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        new_user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=request.POST['password'])
        request.session['user'] = new_user.first_name
        request.session['user_last_name'] = new_user.last_name
        request.session['email'] = new_user.email
        request.session['id'] = new_user.id
        return redirect('/dashboard')
    return redirect('/')

def login(request):
    logged_user = User.objects.filter(email=request.POST['email'])
    if len(logged_user) > 0:
        logged_user = logged_user[0]
        if logged_user.password == request.POST['password']:
            request.session['user'] = logged_user.first_name
            request.session['id'] = logged_user.id
            request.session['email'] = logged_user.email
            return redirect('/dashboard')
    return redirect('/')

def logout(request):
    print(request.session)
    request.session.flush()
    print(request.session)
    return redirect('/')

def cancel(request, golf_id):
    remove = Golf.objects.get(id=golf_id)
    remove.delete()
    return redirect('/dashboard')

def new(request):
    return render(request, 'new_golf.html')

def create_golf(request):
    if request.method == "POST":
        errors = User.objects.golf_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/dashboard')

    Golf.objects.create(
        golf_title = request.POST['golf_title'],
        location = request.POST['location'],
        date = request.POST['date'],
        time = request.POST['time'],
        description = request.POST['description'],
    )    
    return redirect('/dashboard')

def edit(request, golf_id):
    if 'user' not in request.session:
        return redirect('/')
    one_golf = Golf.objects.get(id=golf_id)
    context = {
        'golf': one_golf
    }
    return render(request, 'edit_golf.html', context)

def update(request, golf_id):
    if 'user' not in request.session:
        return redirect('/')
    to_update = Golf.objects.get(id=golf_id)
    errors = Golf.objects.golf_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/edit/{to_update.id}')

    to_update.golf_title = request.POST['golf_title']
    to_update.location = request.POST['location']
    to_update.time = request.POST['time']
    to_update.description = request.POST['description']
    to_update.save()
    return redirect('/dashboard')

def view_golf(request, golf_id):
    if 'user' not in request.session:
        return redirect('/')
    context = {
        'all_golf_by_user': Golf.objects.all(),
    }
    return render(request, 'view_golf.html', context)

def done_with_golf(request, golf_id):
    if 'user' not in request.session:
        return redirect('/')
    remove = Golf.objects.get(id=golf_id)
    remove.delete()
    return redirect('/dashboard')

def add_to_my_golf(request, golf_id):
    if 'user' not in request.session:
        return redirect('/')
    to_add_to_my_golf = Golf.objects.get(id=golf_id)
    to_add_to_my_golf.assigned_golfer = request.session['email']
    to_add_to_my_golf.my_golf_group = True
    to_add_to_my_golf.save()
    return redirect('/dashboard')

def profile(request, user_id):
    if 'user' not in request.session:
        return redirect('/')
    user_id = User.objects.get(id=request.session['id'])
    context = {
        # 'user_profile': User.objects.filter(id=user_id),
        # 'user_golf': User.all_golf_by_user.all(),
        'all_golf_by_user': Golf.objects.all(),
    }
    return render(request, 'profile.html', context)

def create_profile(request):
    if request.method == "POST":
        errors = Profile.objects.profile_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/dashboard')

    Profile.objects.create(
        favorite_golfer = request.POST['favorite_golfer'],
        handicap = request.POST['handicap'],
        description = request.POST['description'],
    )    
    return redirect('/dashboard')

def edit_profile(request, profile_id):
    if 'user' not in request.session:
        return redirect('/')
    user_profile = Profile.objects.get(id=profile_id)
    context = {
        'user_profile': user_profile,
    }
    return render(request, 'edit_profile.html', context)

def update_profile(request, profile_id):
    if 'user' not in request.session:
        return redirect('/')
    to_update = Profile.objects.get(id=profile_id)
    errors = Profile.objects.profile_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/edit/{to_update.id}')

    to_update.favorite_golfer = request.POST['favorite_golfer']
    to_update.handicap = request.POST['handicap']
    to_update.description = request.POST['description']
    to_update.save()
    return redirect('/dashboard')