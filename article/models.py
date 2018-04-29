from django.contrib.auth.models import User
from django.db import models
from tinymce import HTMLField



CHOICE_SUBJECT= (
		('Angular', 'Angular'),
		('Ionic', 'Ionic'),
		('Drf', 'Drf'),
		('Other', 'Other'),
	)

class Article(models.Model):
	title = models.CharField(max_length=100)
	slug = models.SlugField(max_length=140, unique=True)
	subject = models.CharField(max_length=100, default='Other', choices=CHOICE_SUBJECT)
	meta_tag = models.CharField(max_length=100)
	description = models.CharField(max_length=200)
	content = HTMLField('Content')
	author = models.ForeignKey(User)

	class Meta:
		ordering = ['-id']
		verbose_name_plural = 'Articles'

	def __str__(self):
		return self.title

	def _get_unique_slug(self):
		slug = slugify(self.title)
		unique_slug = slug
		num = 1
		while Article.objects.filter(slug=unique_slug).exists():
			unique_slug = '{}-{}'.format(slug, num)
			num += 1
		return unique_slug

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = self._get_unique_slug()
		super().save()


class Comment(models.Model):
	author = models.ForeignKey(User)
	article = models.ForeignKey(Article)
	content = models.TextField()

	class Meta:
		ordering = ['-id']
		verbose_name_plural = 'Comments'

	def __str__(self):
		return self.author.username