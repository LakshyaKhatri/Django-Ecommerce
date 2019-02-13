from django.db import models
import random
import os
# Create your models here.


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    new_filename = random.randint(1, 3910209312)
    name, ext = get_filename_ext(filename)
    final_filename = "{new_filename}{ext}".format(new_filename=new_filename, ext=ext)
    return "products/{final_filename}".format(final_filename=final_filename)


class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=20, default=00.0)
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title