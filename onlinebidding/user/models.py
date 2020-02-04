from django.db import models

# Create your models here.
class UserregisterModel(models.Model):
    idno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    contact = models.IntegerField(unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=30)
    status = models.CharField(max_length=30)
    doj = models.DateField(auto_now_add=True)



class SellProductModel(models.Model):
    id = models.AutoField(primary_key=True)
    pname = models.CharField(max_length=50)
    bid_price = models.FloatField()
    info = models.TextField()
    p_image = models.ImageField(upload_to='products/')
    status = models.CharField(max_length=30)
    user_id = models.ForeignKey(UserregisterModel,on_delete=models.CASCADE)


class BidtableModel(models.Model):
    bidid = models.AutoField(primary_key=True)
    bid_ammount = models.FloatField()
    userid = models.ForeignKey(UserregisterModel,on_delete=models.CASCADE)
    productid = models.ForeignKey(SellProductModel,on_delete=models.CASCADE)
    date_of_join = models.DateField(auto_now_add=True)
    time_of_join = models.TimeField(auto_now_add=True)




