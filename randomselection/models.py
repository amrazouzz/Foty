
from django.db import models




# Create your models here.
class Selection(models.Model):
    num = []
    for i in range(2,9):
        iS = i
        iSS = (iS,iS)
        num.insert(i,iSS)
    
    NUMBERS = tuple(num)

    name = models.CharField(max_length=50,null=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    # teams = models.IntegerField(null=True,choices=NUMBERS)
    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=50, null=True)
    def __str__(self):
        return self.name

class Player(models.Model):
    POSITION= (
        ('حارس','حارس'),
        ('دفاع', 'دفاع'),
        ('وسط','وسط'),
        ('هجوم','هجوم')
    )
    num = []
    for i in range(1,100):
        iS = i
        iSS = (iS,iS)
        num.insert(i,iSS)
    
    NUMBERS = tuple(num)


    name = models.CharField(max_length=50,null=True,)
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    position = models.CharField(max_length=200,null=True,choices=POSITION)
    number = models.IntegerField(null=True,choices=NUMBERS,unique=True)
    def __str__(self):
        return self.name

