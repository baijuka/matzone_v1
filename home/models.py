from django.db import models

# Contact form details
class Contact(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.first_name