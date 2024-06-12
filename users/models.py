from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import RegexValidator



class Profile(models.Model):
    GENDER_CHOICES = (
        ('M', 'Mężczyzna'),
        ('K', 'Kobieta'),
        ('I', 'Inna'),
        ('X', 'Wolę nie podawać'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.FileField(null=True, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    name = models.CharField(null=True, max_length=50, blank=True, validators=[RegexValidator(regex='^[a-zA-ZàáâäãåąčćęèéêëėįìíîïłńòóôöõøùúûüųūÿýżźñçčšžæÀÁÂÄÃÅĄĆČĖĘÈÉÊËÌÍÎÏĮŁŃÒÓÔÖÕØÙÚÛÜŲŪŸÝŻŹÑßÇŒÆČŠŽ∂ð ,.\'-]+$')])
    surname = models.CharField(null=True, max_length=50, blank=True, validators=[RegexValidator(regex='^[a-zA-ZàáâäãåąčćęèéêëėįìíîïłńòóôöõøùúûüųūÿýżźñçčšžæÀÁÂÄÃÅĄĆČĖĘÈÉÊËÌÍÎÏĮŁŃÒÓÔÖÕØÙÚÛÜŲŪŸÝŻŹÑßÇŒÆČŠŽ∂ð ,.\'-]+$')])
    website = models.CharField(null=True, max_length=100, blank=True)
    gender = models.CharField(null=True, max_length=1, choices=GENDER_CHOICES, blank=True)
    phone = models.CharField(null=True, max_length=20, validators=[RegexValidator(regex='^(\+?\d{1,3})?[-.\s]?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$')])
    time_zone = models.CharField(null=True, max_length=100, blank=True, default='Europe/Warsaw')
    country = models.CharField(null=True, max_length=100, blank=True, default='Poland')
    voivodeship = models.CharField(null=True, max_length=30, blank=True)
    city = models.CharField(null=True, max_length=30, blank=True)
    postcode = models.CharField(null=True, max_length=5, blank=True)
    street = models.CharField(null=True, max_length=30, blank=True)
    street_no = models.CharField(null=True, max_length=5, blank=True)
    house_no = models.CharField(null=True, max_length=5, blank=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()