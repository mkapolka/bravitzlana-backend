import uuid

from django.db import models


def generate_save_path(game, filename):
    return 'games/%s/%s' % (game.uuid, filename)


class Game(models.Model):
    session_key = models.CharField(max_length=128, null=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=128, default='')
    description = models.TextField(default='')
    save_data = models.FileField(upload_to=generate_save_path)
    is_new_template = models.BooleanField(default=False)
    is_tutorial_game = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


class Save(models.Model):
    session_id = models.CharField(max_length=128)
    game = models.ForeignKey(Game, related_name='saves')
    save_data = models.FileField(upload_to='saves/')

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
