from django.db import models


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=254)
    email = models.EmailField()
    subject = models.CharField(max_length=254)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.subject} from {self.email}"


class Project(models.Model):
    title = models.CharField(max_length=254)
    image = models.FileField(upload_to="images/")
    description = models.CharField(max_length=254)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"
