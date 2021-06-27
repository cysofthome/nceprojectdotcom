import uuid
from django.db import models
from django.urls import reverse

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
    	return self.name


class Project(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)

    title = models.CharField(max_length=270)
    contents = models.TextField()
    numbers_of_pages = models.IntegerField()
    departments = models.ManyToManyField('Department', related_name='projects')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('project_detail', args=[str(self.id)])


class Feedback(models.Model):
	name = models.CharField(max_length=200)
	email = models.EmailField(max_length=200)
	subject = models.CharField(max_length=200)
	message = models.TextField()


	class Meta:
		verbose_name_plural = 'Feedback'

		def __str__(self):
			return self.name + "-" + self.email
