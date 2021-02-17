from django.db import models

# Create your models here.
class signup(models.Model):
    fnm=models.CharField(max_length=50)
    lnm=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    zip1=models.IntegerField()
                      
    def __str__(self):
        return self.fnm

class post(models.Model):
    title=models.CharField(max_length=50)
    category=models.CharField(max_length=50)
    image=models.FileField(upload_to='upload')
    cmnt=models.CharField(max_length=500)

    def __str__(self):
        return self.title

class reviews(models.Model):
    unm=models.CharField(max_length=50)
    feedback=models.CharField(max_length=500)

    def __str__(self):
        return self.unm


class category(models.Model):
    c_nm=models.CharField(max_length=50)

    def __str__(self):
        return self.c_nm
