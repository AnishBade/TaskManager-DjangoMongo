from djongo import models

# Create your models here.

class Todo(models.Model):
    headline = models.CharField(max_length=255)
    is_completed = models.BooleanField(default=False)

class Task(models.Model):
	title = models.CharField(max_length=200)
	complete = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title
