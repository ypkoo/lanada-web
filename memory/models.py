from __future__ import unicode_literals

from django.db import models

# Create your models here.

# def photo_directory_path(instance, filename):
# 	return 'memory/{0}_{1}/{2}'.format(instance.memory.date.strftime(%y%m%d), instance.memory.title, filename)

# def thumbnail_directory_path(instance, filename):
# 	return 'memory/{0}_{1}/thumbnail_{2}'.format(instance.memory.date.strftime(%y%m%d), instance.memory.title, filename)

# @python_2_unicode_compatible
# class Memory(models.Model):
# 	title = models.CharField(max_length=50)
# 	date = models.DateField()
# 	main_photo = models.ImageField(upload_to=photo_directory_path)
# 	main_thumbnail = models.ImageField(upload_to=thumbnail_directory_path, editable=False)

# 	def save(self, *args, **kwargs):
# 		if self.main:
# 			pass
# 		super(Memory, self).save(*args, **kwargs)

# 	def __str__(self):
# 		return self.title


# class Photo(models.Model):
# 	memory = models.ForeignKey('Memory', on_delete=models.CASCADE)
# 	photo_file = models.ImageField(upload_to=photo_directory_path)
