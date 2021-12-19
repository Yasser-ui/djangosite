from django.conf import settings
from django.db import models
from django.utils import timezone

class Reserve(models.Model):
    #author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.IntegerField()
    resaDate = models.DateField()
    guestNumbr = models.PositiveIntegerField()
    timeFrom = models.TimeField()
    timeTo = models.TimeField()
    comment = models.TextField()
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.phone