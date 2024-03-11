from django.db import models

# Create your models here.
class product(models.Model):
    prodnr = models.IntegerField(primary_key=True)
    prodname = models.TextField()
    prodtype = models.TextField()
    available_quantity = models.IntegerField()

    def __str__(self):
        return self.prodname

class purchase_order(models.Model):
    ponr = models.IntegerField(primary_key=True)
    podate = models.DateField()
    supnr = models.IntegerField()

    def __str__(self):
        return self.ponr

class supplier(models.Model):
    supnr = models.IntegerField(primary_key=True)
    supname = models.TextField(max_length=255)
    supaddress = models.TextField(max_length=255)
    supcity = models.TextField(max_length=255)
    supstatus = models.IntegerField(null=True)

    def __str__(self):
        return self.supname

class supplies(models.Model):
    supnr = models.IntegerField()
    prodnr = models.IntegerField()
    purchase_price = models.FloatField()
    deliv_period = models.TextField(max_length=255)


class po_line(models.Model):
    ponr = models.IntegerField()
    prodnr = models.IntegerField()
    quantity = models.IntegerField()

class chatlog(models.Model):
    chatlognr = models.AutoField(primary_key=True)
    session_id = models.TextField()
    username = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    prompt = models.TextField()
    mode = models.TextField()
    response = models.TextField()
    