from django.db import models
from django.contrib.auth.models import AbstractUser
from phone_field import PhoneField
from datetime import datetime

from django.db.models.signals import post_save
from django.conf import settings
from django.urls import reverse
from django.core.validators import MaxValueValidator,MinValueValidator
from django.dispatch import receiver
# Create your models here.


class User(AbstractUser):
    phone = PhoneField(blank=True, help_text='Contact phone number')
    time = models.DateTimeField(verbose_name="Time", default=datetime.now)


class Gifters(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class ConfirmImage(models.Model):
    upload = models.FileField(upload_to="media", blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Profile(models.Model):
    phone = models.CharField(max_length=13)
    account_details = models.CharField(max_length=1000, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.username


class Gifting(models.Model):
    DEFAULT = 0
    FIRST_PAYMENT = 1
    SECOND_PAYMENT = 2
    THIRD_PAYMENT = 3
    FOURTH_PAYMENT = 4
    FIFTH_PAYMENT = 5

    USERS_WALLET = (
                        (DEFAULT, "default"),
                        (FIRST_PAYMENT, "first payment"),
                        (SECOND_PAYMENT, "second payment"),
                        (THIRD_PAYMENT, "THIRD payment"),
                        (FOURTH_PAYMENT, "FOURTH payment"),
                        (FIFTH_PAYMENT, "FIFTH PAYMENT"),
                    )
    gifting = models.PositiveSmallIntegerField(verbose_name="Withdraw Frequecy", choices=USERS_WALLET)
    username = models.CharField(blank=True, max_length=200)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.username

class Receiving(models.Model):
    DEFAULT = 0
    RECEIVING_ONE = 1
    RECEIVING_TWO = 2
    RECEIVING_THREE = 3
    RECEIVING_FOUR = 4
    RECEIVING_FIVE = 5

    USERS_WALLET = (
                        (DEFAULT, "default"),
                        (RECEIVING_ONE, "recieving one"),
                        (RECEIVING_TWO, "recieving two"),
                        (RECEIVING_THREE, "recieving three"),
                        (RECEIVING_FOUR, "recieving four"),
                        (RECEIVING_FIVE, "recieving five"),
                    )
    receiver = models.PositiveSmallIntegerField(verbose_name="Withdraw Frequecy", choices=USERS_WALLET)
    username = models.CharField(blank=True, max_length=200)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.username


