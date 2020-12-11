from django.db import models
from django.contrib.auth.models import User


class formations(models.Model):
    att=models.IntegerField(default=0,null=True)
    mid_att=models.IntegerField(default=0,null=True)
    mid_mid=models.IntegerField(default=0,null=True)
    mid_def=models.IntegerField(default=0,null=True)
    deff=models.IntegerField(default=0,null=True)
    gk=models.IntegerField(default=1,null=True)
    name = models.CharField(max_length=10,null=True)
    def __str__(self):
        return self.name

class saved_squad(models.Model):
    p1 = models.CharField(max_length=30,null=True,default="none")
    p2 = models.CharField(max_length=30,null=True,default="none")
    p3 = models.CharField(max_length=30,null=True,default="none")
    p4 = models.CharField(max_length=30,null=True,default="none")
    p5 = models.CharField(max_length=30,null=True,default="none")
    p6 = models.CharField(max_length=30,null=True,default="none")
    p7 = models.CharField(max_length=30,null=True,default="none")
    p8 = models.CharField(max_length=30,null=True,default="none")
    p9 = models.CharField(max_length=30,null=True,default="none")
    p10 = models.CharField(max_length=30,null=True,default="none")
    p11 = models.CharField(max_length=30,null=True,default="none") 
    formation = models.ForeignKey(formations,null=True,on_delete=models.CASCADE)
    name=models.CharField(max_length=30,null=True) 
    user=models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username+" / "+self.name


class temp(models.Model):
    user=models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    form = models.ForeignKey(formations,null=True,on_delete=models.CASCADE)
    names = models.TextField()
    def __str__(self):
        return self.user.username+" / "+self.form.name

