from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Registration(models.Model):
    """For gmail registration"""
    user = models.ForeignKey(User, related_name="user_info", on_delete=models.CASCADE)
    phone = models.IntegerField()
    dob = models.DateField(max_length=8)
    is_spam  = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user.first_name)

    objects = models.Manager()


class Mails(models.Model):
    """To store the mails"""
    sender = models.ForeignKey(Registration, related_name="sender_mail", on_delete=models.CASCADE)
    receiver = models.EmailField(blank=True, null=True)
    subject = models.CharField(max_length=100)
    body = models.TextField(max_length=500)
    is_draft = models.BooleanField(default=False)

    def __str__(self):
        return str(self.sender)

    objects = models.Manager()
