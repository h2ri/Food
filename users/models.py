from django.db import models
from django.db.models.signals import post_save
from django.conf import settings
from oauth2_provider.models import Application

from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

GENDER = (
    ('M', 'Male'),
    ('F', 'Female'),
)

class MyUserManager(BaseUserManager):
    def create_user(self, username,email, password=None):
        print username
        if not email:
            email = username + "@hari.com"

        user = self.model(
            username = username,
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username,email, password):
        user = self.create_user(username,
                                email,
                                password=password,
                                )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    username = models.CharField(max_length=20)
    phone = models.CharField(max_length=10)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    about = models.TextField(null=True, blank=True)
    gender = models.CharField(
        max_length=1, null=True, blank=True, choices=GENDER)
    date_of_birth = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    #REQUIRED_FIELDS = ['date_of_birth']

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def get_display_name(self):
        return self.first_name

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def __str__(self):  # __unicode__ on Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

    @property
    def is_superuser(self):
        return self.is_admin


class UserInfo(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='UserInfo')
    address = models.CharField(max_length=255)
    addressLocality = models.CharField(max_length=255,blank=True,null=True)
    addressSubLocality = models.CharField(max_length=100, blank=True,null=True)
    addressLatitude = models.FloatField(blank=True,null=True)
    addressLogitude = models.FloatField(blank=True,null=True)
    created_at_time = models.DateTimeField(auto_now_add=True, blank=True)
    flag = models.BooleanField(default=0, blank=True)

'''def create_auth_client(sender, instance=None, created=False, **kwargs):
    if created:
        Application.objects.create(user=instance, client_type=Application.CLIENT_CONFIDENTIAL,
                                   authorization_grant_type=Application.GRANT_PASSWORD)

post_save.connect(create_auth_client, sender=settings.AUTH_USER_MODEL)
'''