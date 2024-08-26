from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=255)
    email = models.ForeignKey("addresses.Address", on_delete=models.CASCADE, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
