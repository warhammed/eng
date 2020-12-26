from django.db import models
from django.urls import reverse

class Group(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField()

    class Meta:
        verbose_name = "گروه"
        verbose_name_plural = "گروه ها"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("groups:group", kwargs={"pk": self.pk})