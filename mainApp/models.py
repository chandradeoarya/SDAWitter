from django.db import models
import re


class UserManager(models.Manager):
    def validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        emails = Users.objects.filter(email__iexact=postData['email'])
        usernames = Users.objects.filter(username__iexact=postData['username'])
        if len(emails)>0 or len(usernames)>0:
            if len(emails)>0:
                errors['emailExist']="This Email is already in use!"
            if len(usernames)>0:
                errors['usernameExist']='This Username is already taken!'
            return errors
        if len(postData['username'])<6:
            errors['username']='Username must be at least 6 characters'
        if len(postData['fname'])<2:
            errors['fname']='First Name must be at least 2 characters'
        if len(postData['lname'])<2:
            errors['lname']='Last Name must be at least 2 characters'
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email address!"
        if len(postData['password'])<8:
            errors['password']='Password must be at least 8 characters'
        if not postData['password'] == postData['Cpassword']:
            errors['Cpassword']='Password and Confirm Password must be the same!'
        return errors

class PostManager(models.Manager):
    def validator(self, postData):
        errors = {}
        if len(postData['content'])<1:
            errors['content']='Content must be at least 1 characters'
        return errors

class Users(models.Model):
    username = models.CharField(max_length=255)
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Posts(models.Model):
    user = models.ForeignKey(Users, related_name='posts', on_delete=models.CASCADE)
    content = models.TextField(max_length=281)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    objects = PostManager()