from django.db import models

# Create your models here.
class UsersApp(models.Model):
    name = models.CharField(max_length=50, null=False)
    password = models.CharField(max_length=200, null=False)
    
    def __str__(self):
        return str(self.name)


class Quizzes(models.Model):
    name=models.CharField(max_length=20, null=False)
    user_app=models.ForeignKey(UsersApp,null=True,blank=True,on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.name)