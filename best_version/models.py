from django.db import models


class Goal(models.Model):
    id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=200)
    best_version = models.CharField(max_length=100)
    goal_text = models.CharField(max_length=200)
    goal_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.goal_text

class ProudMoment(models.Model):
    id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=200)
    best_version = models.CharField(max_length=200)
    proud_moment_text = models.CharField(max_length=500)

class BestMoment(models.Model):
    id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=200)
    best_version = models.CharField(max_length=200)
    best_moment_text = models.CharField(max_length=500)

class Version(models.Model):
    id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=200)
    best_version = models.CharField(max_length=200)

class TempMoment(models.Model):
    id = models.AutoField(primary_key=True)
    temp_moment = models.CharField(max_length=500)