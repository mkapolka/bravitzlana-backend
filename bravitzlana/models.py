from django.db import models


class Game(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    save_data = models.FileField(upload_to='games/')

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


class Save(models.Model):
    session_id = models.CharField(max_length=128)
    game = models.ForeignKey(Game, related_name='saves')
    save_data = models.FileField(upload_to='saves/')

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
