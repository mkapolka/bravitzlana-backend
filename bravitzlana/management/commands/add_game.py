import os

from django.core.management.base import BaseCommand, CommandError
from django.core.files import File

from bravitzlana.models import Game


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--file', dest='filename', type=str)
        parser.add_argument('--name', type=str)
        parser.add_argument('--description', type=str, default='')
        parser.add_argument('--is_new_template', action='store_true')

    def handle(self, filename, name, description, is_new_template, *args, **kwargs):
        if not os.path.exists(filename):
            raise CommandError("File does not exist.")
        with open(filename, 'r') as file_handle:
            dj_file = File(file_handle)
            game = Game.objects.create(name=name,
                                       description=description,
                                       is_new_template=is_new_template,
                                       save_data=dj_file)
            print("Game UUID: %s" % game.uuid)
