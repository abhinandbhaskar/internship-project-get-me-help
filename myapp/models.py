from django.db import models

# Create your models here.

class login(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=40)
    usertype=models.CharField(max_length=30)


class user(models.Model):
    name=models.CharField(max_length=40)
    place=models.CharField(max_length=50)
    pin=models.CharField(max_length=10)
    post=models.CharField(max_length=50)
    email=models.CharField(max_length=40)
    phone=models.CharField(max_length=20)
    image=models.CharField(max_length=250)
    LOGIN=models.ForeignKey(login,on_delete=models.CASCADE)



class worker(models.Model):
    worker_name=models.CharField(max_length=40)
    email=models.CharField(max_length=40)
    phone=models.CharField(max_length=20)
    image=models.CharField(max_length=250)
    LOGIN=models.ForeignKey(login,on_delete=models.CASCADE)



class complaints(models.Model):
    complaint=models.CharField(max_length=500)
    date=models.CharField(max_length=20)
    reply=models.CharField(max_length=300)
    reply_date=models.CharField(max_length=20)
    USER=models.ForeignKey(user,on_delete=models.CASCADE)


class feed_backs(models.Model):
    feedback=models.CharField(max_length=500)
    date=models.CharField(max_length=20)
    USER=models.ForeignKey(user,on_delete=models.CASCADE)
    WORKER=models.ForeignKey(worker,on_delete=models.CASCADE)


class services(models.Model):
    service_name=models.CharField(max_length=40)


class own_services(models.Model):
    WORKER=models.ForeignKey(worker,on_delete=models.CASCADE)
    amount=models.CharField(max_length=30)
    SERVICE=models.ForeignKey(services,on_delete=models.CASCADE)


class work_request(models.Model):
    date=models.CharField(max_length=20)
    status=models.CharField(max_length=30)
    USER=models.ForeignKey(user,on_delete=models.CASCADE)
    OWNSERVICES=models.ForeignKey(own_services,on_delete=models.CASCADE)



class bank(models.Model):
    bank_name=models.CharField(max_length=100)
    accnt_no=models.CharField(max_length=25)
    ifsc_code=models.CharField(max_length=30)
    branch_name=models.CharField(max_length=40)
    balance=models.CharField(max_length=30)
    LOGIN=models.ForeignKey(login,on_delete=models.CASCADE)



class PaymentStatus(models.Model):
    bankname = models.CharField(max_length=50)
    paymnt_sts = models.CharField(max_length=40)
    date = models.CharField(max_length=30)
    OWNSERVICES = models.ForeignKey(own_services, on_delete=models.CASCADE, default=1)  # Adjust the default value as needed
    USER = models.ForeignKey(user, on_delete=models.CASCADE, default=1)











