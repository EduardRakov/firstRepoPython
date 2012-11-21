from django.db import models

# Create your models here.

class Page(models.Model):
        def __init__(self, *args, **kwargs):
            super(Page, self).__init__(*args, **kwargs)
            self.contents = None
        name = models.CharField(max_length=20, primary_key=True)
        content = models.TextField(blank=True)
