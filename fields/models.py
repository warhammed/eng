from django.db import models
from django.urls import reverse

class Field(models.Model):
    degree = models.ForeignKey("fields.Degree", on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    slug = models.SlugField(allow_unicode=True)

    class Meta:
        verbose_name = "Field"
        verbose_name_plural = "Fields"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Field_detail", kwargs={"pk": self.pk})

class Degree(models.Model):

    name = models.CharField(max_length=50)
    slug = models.SlugField()

    class Meta:
        verbose_name = "Degree"
        verbose_name_plural = "Degrees"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Degree_detail", kwargs={"pk": self.pk})
