from django.db import models

class User(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    # Add other fields as needed

class Team(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(User)

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

class Leaderboard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()

class Workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=100)
    duration = models.IntegerField()