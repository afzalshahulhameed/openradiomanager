from django.db import models
from django.core.urlresolvers import reverse

class Station(models.Model):
    name = models.CharField(max_length=50)
    address = models.TextField(default='')
    
    def get_absolute_url(self):
        return reverse("viewstation", kwargs={"pk": self.pk})
        
class Channel(models.Model):
    c_name = models.CharField(max_length=50)
    c_frequency = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse("viewchannel", kwargs={"pk": self.pk})
