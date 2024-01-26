from django.db import models

# Create your models here.

class signup_tbl(models.Model):
    nm=models.CharField(max_length=50)
    em=models.EmailField()
    pn=models.IntegerField()
    np=models.CharField(max_length=8)
    cp=models.CharField(max_length=8)
    def __str__(self):
        return self.nm
    
class Record(models.Model):
    creation_date=models.DateTimeField(auto_now_add=True)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone=models.IntegerField()
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    province=models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    zipcode=models.IntegerField()

    def __str__(self):
        return self.first_name + "  " +self.last_name