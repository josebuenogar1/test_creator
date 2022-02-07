from msilib.schema import Class
from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=50, null=False)
    def __str__(self):
        return str(self.name)


class Quiz(models.Model):
    name=models.CharField(max_length=20, null=False)
    user_app=models.ForeignKey(Profile,null=True,blank=True,on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.name)

class QuizOptions(models.Model):
    sentence=models.CharField(max_length=50, null=False, unique=True)
    true_answer=models.CharField(max_length=50, null=False)
    false_anser_one=models.CharField(max_length=50, null=False)
    false_anser_two=models.CharField(max_length=50, null=False)

    def __str__(self):
        return str(self.sentence)

    @property
    def get_true_answer(self):
        return str(self.true_answer)

    @property
    def get_false_anser_one(self):
        return str(self.false_anser_one)

    @property
    def get_false_anser_two(self):
        return str(self.false_anser_two)

class QuizType(models.Model):
    name=models.CharField(max_length=20 , null=False)
    def __str__(self):
        return str(self.name)

class Questions(models.Model):
    number=models.IntegerField()
    quiz_type=models.ForeignKey(QuizType,null=False,blank=False,on_delete=models.DO_NOTHING)
    quiz=models.ForeignKey(Quiz,null=False,blank=False,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.number)


