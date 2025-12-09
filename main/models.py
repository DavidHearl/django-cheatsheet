from django.db import models

class Section(models.Model):
    name = models.CharField(max_length=100)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['order']

class Content(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body = models.TextField()
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']
