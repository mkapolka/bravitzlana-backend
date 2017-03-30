from django.db import transaction
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt

from bravitzlana.models import Game


@csrf_exempt
def upload(request):
    if request.method != 'POST':
        return HttpResponseBadRequest("Malformed upload.")
    with transaction.atomic():
        Game.objects.create(
            name=request.POST['name'],
            description=request.POST['description'],
            save_data=request.FILES['save']
        )
        return HttpResponse("Looks dope dude")


@csrf_exempt
def save_data(request, uuid):
    try:
        game = Game.objects.get(uuid=uuid)
        return HttpResponse(game.save_data, content_type='text/plain')
    except Game.DoesNotExist:
        return HttpResponseNotFound
