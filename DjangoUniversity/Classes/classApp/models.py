from django.db import models


class djangoClasses(models.Model):
    Title = models.CharField(max_length=60, default="", blank=True, null=False)
    courseNumber = models.IntegerField()
    instructorName = models.CharField(max_length=60, default="", blank=True, null=False)
    duration = models.FloatField()

    objects = models.Manager()

    def __str__(self):
        return self.Title
