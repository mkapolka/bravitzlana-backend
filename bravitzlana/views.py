from django.db import transaction
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt

from bravitzlana.models import Game


@csrf_exempt
def upload(request):
    if request.method != 'POST':
        return HttpResponseBadRequest("Malformed upload.")
    with transaction.atomic():
        print(request.POST)
        Game.objects.create(
            name=request.POST['name'],
            description=request.POST['description'],
            save_data=request.FILES['save']
        )
        return HttpResponse("Looks dope dude")
