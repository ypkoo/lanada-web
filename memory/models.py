from __future__ import unicode_literals

from cStringIO import StringIO
import os
from django.db import models
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage as storage
from django.utils.encoding import python_2_unicode_compatible

from PIL import Image
THUMB_SIZE = (320, 180)

# Create your models here.

def photo_directory_path(instance, filename):
	return 'memory/{0}_{1}/{2}'.format(instance.date.strftime("%y%m%d"), instance.title, filename)

def photo_child_directory_path(instance, filename):
	return 'memory/{0}_{1}/{2}'.format(instance.memory.date.strftime("%y%m%d"), instance.memory.title, filename)

def thumbnail_directory_path(instance, filename):
	# return 'memory/{0}_{1}/{2}'.format(instance.date.strftime("%y%m%d"), instance.title, filename)
	return filename

@python_2_unicode_compatible
class Memory(models.Model):
	title = models.CharField(max_length=50)
	date = models.DateField()
	main_photo = models.ImageField(upload_to=photo_directory_path)
	main_thumbnail = models.ImageField(upload_to=thumbnail_directory_path, editable=False)
	# main_thumbnail = models.ImageField(upload_to='/', editable=False)

	def save(self, *args, **kwargs):
		super(Memory, self).save(*args, **kwargs)
		if not self.make_thumbnail():
			raise Exception('Could not create thumbnail - is the file type valid?')
		super(Memory, self).save(*args, **kwargs)

	def make_thumbnail(self):
		"""
		Create and save the thumbnail for the photo (simple resize with PIL).
		"""

		fh = storage.open(self.main_photo.name, 'r')
		try:
			image = Image.open(fh)
		except:
			return False

		image.thumbnail(THUMB_SIZE, Image.ANTIALIAS)
		fh.close()

		# Path to save to, name, and extension
		thumb_name, thumb_extension = os.path.splitext(self.main_photo.name)
		thumb_extension = thumb_extension.lower()

		thumb_filename = thumb_name + '_thumb' + thumb_extension

		if thumb_extension in ['.jpg', '.jpeg']:
			FTYPE = 'JPEG'
		elif thumb_extension == '.gif':
			FTYPE = 'GIF'
		elif thumb_extension == '.png':
			FTYPE = 'PNG'
		else:
			return False    # Unrecognized file type

		# Save thumbnail to in-memory file as StringIO
		temp_thumb = StringIO()
		image.save(temp_thumb, FTYPE)
		temp_thumb.seek(0)

		# Load a ContentFile into the thumbnail field so it gets saved
		self.main_thumbnail.save(thumb_filename, ContentFile(temp_thumb.read()), save=False)
		temp_thumb.close()

		return True

	def __str__(self):
		return self.title

@python_2_unicode_compatible
class Photo(models.Model):
	memory = models.ForeignKey('Memory', on_delete=models.CASCADE)
	photo_file = models.ImageField(upload_to=photo_child_directory_path)

	def __str__(self):
		return self.photo_file.name
