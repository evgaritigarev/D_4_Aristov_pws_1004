from django.db import models

class Article(models.Model):
    name = models.CharField(max_length=128)
    dateCreation = models.DateTimeField(auto_now_add=True)
    post = models.TextField()

    def __str__(self):
        return f'{self.name.title()}'
    
    def get_absolute_url(self):
        return f'/article/{self.id}'
