from django.db import models
from django.contrib.auth.models import User


class BaseModel(models.Model):

    class Meta:
        abstract = True

    active = models.BooleanField(default=True)
    created_by = models.ForeignKey(
        User,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name="%(class)s_created_by",
    )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(
        User,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name="%(class)s_updated_by"
    )
    updated_on = models.DateTimeField(auto_now=True)