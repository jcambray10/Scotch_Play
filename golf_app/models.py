from time import time
import datetime
from django.db import models
import re
import bcrypt
from django.forms import CharField

class UserManager(models.Manager):
    def basic_validator(self, postdata):
        errors = {}
        if len(postdata['first_name']) < 2:
            errors['first_name'] = "First name must be at least two characters long"
        if len(postdata['last_name']) < 2:
            errors['last_name'] = "Last name must be at least two characters long"
        
        email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(postdata['email'])== 0:
            errors['email'] = "You must enter an email"
        elif not email_regex.match(postdata['email']):
            errors['email'] = "Must be a valid email"
        
        current_users = User.objects.filter(email = postdata['email'])
        if len(current_users) > 0:
            errors['duplicate'] = "That email is already in use"

        if len(postdata['password']) < 8:
            errors['password'] = "Password must be at least 8 characters long"
        if postdata['password'] != postdata['confirm_password']:
            errors['mismatch'] = "Your passwords do not match"
        return errors

    def login_validator(self, postdata):
        errors= {}
        existing_user = User.objects.filter(email=postdata['email'])
        if len(postdata['email']) == 0:
            errors['email'] = "Email must be entered"
        if len(postdata['password']) < 8:
            errors['password'] = "An eight character password must be entered"
        
        elif bcrypt.checkpw(postdata['password'].encode(), existing_user[0].password.encode()) != True:
            errors['password'] = "Email and password do not match"
        return errors

    def golf_validator(self, postdata):
        errors = {}
        if len(postdata['golf_title']) < 3:
            errors['golf_title'] = "A golf title must have more than 3 characters"
        if len(postdata['location']) == 0:
            errors['location'] = "The location must not be blank"
        if len(postdata['date']) == 0:
            errors['date'] = "The date must not be blank"
        if len(postdata['time']) == 0:
            errors['time'] = "The time must not be blank"
        if len(postdata['description']) < 5:
            errors['description'] = "A golf description must have more than 5 characters"
        return errors

class GolfManager(models.Manager):
    def golf_validator(self, postdata):
        errors = {}
        if len(postdata['golf_title']) < 3:
            errors['golf_title'] = "A golf title must have more than 3 characters"
        if len(postdata['location']) == 0:
            errors['location'] = "The location must not be blank"
        if len(postdata['date']) == 0:
            errors['date'] = "The date must not be blank"
        if len(postdata['time']) == 0:
            errors['time'] = "The time must not be blank"
        if len(postdata['description']) < 5:
            errors['description'] = "A golf description must have more than 5 characters"
        return errors

class ProfileManager(models.Manager):
    def profile_validator(self, postdata):
        errors = {}
        if len(postdata['favorite_golfer']) < 5:
            errors['favorite_golfer'] = "A favorite golf must have more than 5 characters"
        if len(postdata['handicap']) == 0:
            errors['handicap'] = "The handicap must not be blank"
        if len(postdata['description']) < 5:
            errors['description'] = "A profile description must have more than 5 characters"

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50) 
    password = models.CharField(max_length=50)
    objects = UserManager()
    # all_golf_by_user = list of all golf for this user

class Golf(models.Model):
    golf_title = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    date = models.CharField(max_length=50)
    time = models.CharField(max_length=50)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    my_golf_group = models.BooleanField(default=False)
    assigned_golfer = models.CharField(max_length=50)
    User = models.ForeignKey(User, related_name='all_golf_by_user', on_delete=models.CASCADE, null=True, blank=True)
    objects = GolfManager()

class Profile(models.Model):
    profile_picture = models.ImageField(null=True, blank=True)
    favorite_golfer = models.TextField()
    handicap = CharField(max_length=10)
    description = models.TextField()
    user = models.OneToOneField(User, related_name ='user_profile', on_delete=models.CASCADE, null=True, blank=True)
    objects = ProfileManager()

# echo "# Scotch_Play" >> README.md
# git init
# git add README.md
# git commit -m "first commit"
# git branch -M main
# git remote add origin https://github.com/jcambray10/Scotch_Play.git
# git push -u origin main