from django.contrib.auth import get_user_model
from django.db import models


class Recipe(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, blank=True)
    recipe_name = models.CharField(max_length=256)
    recipe_url = models.URLField(max_length = 200, null=True, blank=True)
    notes = models.TextField(default="", null=True, blank=True)

    def __str__(self):
        return self.recipe


