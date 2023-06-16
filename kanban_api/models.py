from django.db import models


# Create your models here.

class Admin(models.Model):
    name = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    login = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    def __str__(self):
        return self.name + ' ' + self.lastName

class Board(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=250)
    creatorDate = models.DateTimeField(auto_now_add=True)
    updatedDate = models.DateTimeField(auto_now=True)
    settings = models.TextField(null=True, blank=True)
    adminId = models.ForeignKey('Admin', on_delete=models.CASCADE, related_name='boards', null=True, default=None)

    def __str__(self):
        return self.name


class StatusList(models.Model):
    title = models.CharField(max_length=100)
    countCard = models.IntegerField()
    color =models.CharField(max_length=50)
    boardId = models.ForeignKey('Board', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    

class User(models.Model):
    name = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    login = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    boardId = models.ForeignKey('Board', on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Card(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    color =models.CharField(max_length=50)
    priority = models.IntegerField()
    dueDates = models.DateField()
    statusListId = models.ForeignKey('StatusList', on_delete=models.CASCADE)
    userId = models.ForeignKey('User', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

