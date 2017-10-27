from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class Channel(models.Model):
    channel_name = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "Channel"

    def __str__(self):
        return self.channel_name


class Field(models.Model):
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    field_name = models.CharField(max_length=30)
    data = models.CharField(max_length=20)

    def save(self, *args, **kwargs):
        s = super(Field, self).save(*args, **kwargs)
        FieldHistory(field=self, data=self.data).save()
        return s

    class Meta:
        db_table = "Field"

    def __str__(self):
        return self.field_name


class FieldHistory(models.Model):
    field = models.ForeignKey(Field, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now=True)
    data = models.CharField(max_length=20)

    class Meta:
        db_table = "FieldHistory"

    def __str__(self):
        return self.field.field_name + " " + self.data


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
