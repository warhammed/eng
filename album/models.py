from django.db import models

def album_image_path(instance, filename):
    return 'album/{0}/{1}'.format(instance.album.pk, filename)

class Album(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(allow_unicode=True)
    
    class Meta:
        verbose_name = "آلبوم"
        verbose_name_plural = "آلبوم‌ها"

    def __str__(self):
        return str(self.pk)

class AlbumImage(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=album_image_path)
    caption = models.CharField(max_length=50)

    class Meta:
        verbose_name = "AlbumImage"
        verbose_name_plural = "AlbumImages"

    def __str__(self):
        return str(self.pk)
