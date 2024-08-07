from django.db import models

# Create your models here.
class customer(models.Model):
    plan_category = (
        ('5 year','2 year'),
        ('10 year','1 year'),
        ('1 month','2 month')
    )
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    MobileNumber = models.IntegerField()
    email = models.EmailField()
    plan = models.CharField(max_length=30,choices=plan_category)
