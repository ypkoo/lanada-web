from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.

class AbstractPaper(models.Model):
	title = models.CharField(max_length=50)
	author = models.CharField(max_length=50)
	keywords = models.CharField(max_length=50)
	date = models.DateField()

	class Meta:
		abstract = True

@python_2_unicode_compatible
class ConferencePaper(AbstractPaper):
	conference_name = models.CharField(max_length=50)
	pdf_file_c = models.FileField(upload_to='paper/conference')
	pdf_filename_c = models.CharField(max_length=50, default=None, blank=True, editable=False)

	def save(self, *args, **kwargs):
		if self.pdf_file_c:
			self.pdf_filename_c = self.pdf_file_c.name.split('/')[-1]
		super(ConferencePaper, self).save(*args, **kwargs)

	def __str__(self):
		return self.title

@python_2_unicode_compatible
class JournalPaper(AbstractPaper):
	journal_name = models.CharField(max_length=50)
	pdf_file_j = models.FileField(upload_to='paper/journal')
	pdf_filename_j = models.CharField(max_length=50, default=None, blank=True, editable=False)

	def save(self, *args, **kwargs):
		if self.pdf_file_j:
			self.pdf_filename_j = self.pdf_file_j.name.split('/')[-1]
		super(JournalPaper, self).save(*args, **kwargs)

	def __str__(self):
		return self.title