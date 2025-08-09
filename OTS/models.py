from django.db import models

# Create your models here.

class Candidate(models.Model):
    Username = models.CharField(max_length=100,primary_key=True)
    password = models.CharField(max_length=100,null=False)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    testAttempted = models.IntegerField()
    points = models.FloatField()


    def __str__(self):
        return self.Username
    
class Question(models.Model):
    queID = models.BigAutoField(primary_key=True,auto_created=True)
    question_text = models.TextField()
    a = models.CharField(max_length=100)
    b = models.CharField(max_length=100)
    c = models.CharField(max_length=100)
    d = models.CharField(max_length=100)
    correct_option = models.CharField(max_length=1)  # 'a', 'b', 'c', or 'd'

    def __str__(self):
        return self.question_text

class Result(models.Model):
   resultID = models.BigAutoField(primary_key=True, auto_created=True)
   username = models.ForeignKey(Candidate, on_delete=models.CASCADE)
   date = models.DateField(auto_now=True)
   time = models.TimeField(auto_now=True)
   attempts = models.IntegerField()
   right = models.IntegerField()
   wrong = models.IntegerField()
   points = models.FloatField()


