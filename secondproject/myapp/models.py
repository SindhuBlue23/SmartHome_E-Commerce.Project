from django.db import models

# Create your models here.
class customer (models.Model):
    userid = models.IntegerField()
    cusid = models.BigAutoField(primary_key=True)
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    contactname = models.CharField(max_length=20)

class supplier(models.Model):
    sid = models.BigAutoField(primary_key=True)
    sname = models.CharField(max_length=20)
    semail = models.CharField(max_length=20)
    sphno = models.CharField(max_length=20)

class cusinfo(models.Model):
    cusinfoid = models.BigAutoField(primary_key=True)
    cusid = models.ForeignKey(customer, on_delete=models.CASCADE)
    country = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    phno = models.IntegerField()
    email = models.CharField(max_length=20)
    city = models.CharField(max_length=20)

class admin4(models.Model):
    adminid = models.IntegerField()
    adminname = models.CharField(max_length=20)
    adminpass = models.CharField(max_length=20)

class categories(models.Model):
    cateid = models.BigAutoField(primary_key=True)
    catname = models.CharField(max_length=20)
    description = models.CharField(max_length=20)

class product(models.Model):
    pid = models.BigAutoField(primary_key=True)
    sid = models.ForeignKey(supplier, on_delete=models.CASCADE)
    cateid = models.ForeignKey(categories, on_delete=models.CASCADE)
    pname = models.CharField(max_length=20)
    unitsinstock = models.IntegerField()
    price = models.IntegerField()
    description = models.CharField(max_length=20)
    defaultimage = models.CharField(max_length=500)

class images12(models.Model):
    pid = models.ForeignKey(product, on_delete=models.CASCADE)
    imgid = models.BigAutoField(primary_key=True)
    image = models.FileField(upload_to="Images")

class cart(models.Model):
    cid = models.BigAutoField(primary_key=True)
    noproducts = models.IntegerField()
    tprice = models.IntegerField()
    cusid = models.ForeignKey(customer, on_delete=models.CASCADE)
    pid = models.ForeignKey(product, on_delete=models.CASCADE)

class billing(models.Model):
    bid = models.BigAutoField(primary_key=True)
    cusid = models.ForeignKey(customer, on_delete=models.CASCADE)
    cardname = models.CharField(max_length=20)
    cardnum = models.IntegerField()
    expmonth = models.IntegerField()
    expyear = models.IntegerField()
    cvv = models.IntegerField()

class order(models.Model):
    cusid = models.ForeignKey(customer, on_delete=models.CASCADE)
    oid = models.BigAutoField(primary_key=True)
    odate = models.DateField()
    shipdate = models.DateField()
    ostatus = models.CharField(max_length=20)
    totalprice = models.IntegerField()
    addressid = models.ForeignKey(cusinfo, on_delete=models.CASCADE)
    cardid = models.ForeignKey(billing, on_delete=models.CASCADE)

class ordetails(models.Model):
    oid = models.ForeignKey(order, on_delete=models.CASCADE)
    pid = models.ForeignKey(product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.IntegerField()


