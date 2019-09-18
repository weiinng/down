from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=32)
    publish = models.ForeignKey(to="Publish", related_name="publish")
    authors = models.ManyToManyField(to="Author", related_name="authors")

    def __str__(self):
        return self.title


class Publish(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name
