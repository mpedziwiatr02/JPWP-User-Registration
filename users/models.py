import os
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import RegexValidator
from django.forms import ValidationError


def validate_avatar(file):
    valid_extensions = [".jpg", ".jpeg", ".png", ".gif"]
    file_extension = os.path.splitext(file.name)[1]
    file_size = file.size
    max_file_size = 25 * 1024 * 1024  # 25 MB

    if file_extension.lower() not in valid_extensions:
        raise ValidationError(
            f'Ten format jest niepoprawny. Dostępne formaty: {", ".join(valid_extensions)}.'
        )

    if file_size > max_file_size:
        raise ValidationError(
            f"Ten plik przekracza limit 25 MB. Rozmiar: {file_size / (1024 * 1024):.2f} MB."
        )
    

def user_directory(instance, filename):
    return '{0}/avatar.{1}'.format(instance.user.username, filename.split(".")[-1])


class Profile(models.Model):
    GENDER_CHOICES = (
        ("M", "Mężczyzna"),
        ("K", "Kobieta"),
        ("I", "Inna"),
        ("X", "Wolę nie podawać"),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.FileField(
        null=True,
        blank=True,
        upload_to=user_directory,
        validators=[validate_avatar]
    )
    bio = models.TextField(blank=True, max_length=512)
    birth_date = models.DateField(null=True, blank=True)
    name = models.CharField(
        null=True,
        blank=True,
        max_length=64,
        validators=[
            RegexValidator(
                regex="^[a-zA-ZàáâäãåąčćęèéêëėįìíîïłńòóôöõøùúûüųūÿýżźñçčšžæÀÁÂÄÃÅĄĆČĖĘÈÉÊËÌÍÎÏĮŁŃÒÓÔÖÕØÙÚÛÜŲŪŸÝŻŹÑßÇŒÆČŠŽ∂ð ,.'-]+$"
            )
        ],
    )
    surname = models.CharField(
        null=True,
        blank=True,
        max_length=64,
        validators=[
            RegexValidator(
                regex="^[a-zA-ZàáâäãåąčćęèéêëėįìíîïłńòóôöõøùúûüųūÿýżźñçčšžæÀÁÂÄÃÅĄĆČĖĘÈÉÊËÌÍÎÏĮŁŃÒÓÔÖÕØÙÚÛÜŲŪŸÝŻŹÑßÇŒÆČŠŽ∂ð ,.'-]+$"
            )
        ],
    )
    website = models.CharField(null=True, blank=True, max_length=128)
    gender = models.CharField(null=True, blank=True, max_length=1, default="X")
    phone = models.CharField(
        null=True,
        blank=True,
        max_length=32,
        validators=[
            RegexValidator(
                regex=r"^([+]?[\s0-9]+)?(\d{3}|[(]?[0-9]+[)])?([-]?[\s]?[0-9])+$"
            )
        ],
    )
    time_zone = models.CharField(
        null=True, blank=True, max_length=64, default="Europe/Warsaw"
    )
    country = models.CharField(null=True, blank=True, max_length=64, default="Poland")
    region = models.CharField(null=True, blank=True, max_length=64)
    city = models.CharField(null=True, blank=True, max_length=64)
    postcode = models.CharField(
        null=True,
        blank=True,
        max_length=16,
        validators=[RegexValidator(regex="^[0-9-]*$")],
    )
    street = models.CharField(null=True, blank=True, max_length=64)
    street_no = models.CharField(
        null=True,
        blank=True,
        max_length=8,
        validators=[RegexValidator(regex="^[0-9]+$")],
    )
    house_no = models.CharField(
        null=True,
        blank=True,
        max_length=8,
        validators=[RegexValidator(regex="^[0-9]+$")],
    )


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
