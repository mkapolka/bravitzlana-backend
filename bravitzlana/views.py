import uuid

from django.db import transaction
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotFound, HttpResponseServerError
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from bravitzlana.models import Game


@csrf_exempt
def upload(request):
    if request.method != 'POST':
        return HttpResponseBadRequest("Malformed upload.")
    try:
        with transaction.atomic():
            game = Game.objects.create(
                name=request.POST['name'],
                description=request.POST['description'],
                save_data=request.FILES['save']
            )
            return HttpResponse(request.build_absolute_uri(reverse('play', args=[game.uuid])))
    except Exception as e:
        return HttpResponseServerError(str(e))


@csrf_exempt
def save_data(request, uuid):
    try:
        game = Game.objects.get(uuid=uuid)
        return HttpResponse(game.save_data, content_type='text/plain')
    except Game.DoesNotExist:
        return HttpResponseNotFound


def play(request, uuid, uuid_override=None):
    try:
        game = Game.objects.get(uuid=uuid)
        context = {
            'uuid': game.uuid,
            'name': game.name,
            'description': game.description
        }
        if uuid_override:
            context['uuid_override'] = uuid_override
        return render(request, 'player/index.html', context)
    except Game.DoesNotExist:
        return HttpResponseNotFound


def new(request, uuid_override):
    if not uuid_override:
        return redirect('new', uuid.uuid4())
    else:
        return play(request, Game.objects.filter(is_new_template=True)[0].uuid, uuid_override)


def games(request):
    context = {
        'games': Game.objects.order_by('-created')[:10]
    }
    return render(request, 'games.html', context)
