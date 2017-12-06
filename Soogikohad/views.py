from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from Soogikohad import models


def index(request):
    soogikohad = models.Soogikohad.objects.all()
    context = {'soogikohad': soogikohad}
    return render(request, 'index.html', context)


def get_soogikohad(request):
    soogikohad = models.Soogikohad.objects.all().values('nimi', 'lat', 'lng', 'eelroad', 'supid', 'praed',
                                                        'magustoidud', 'joogid', 'kohvilaud', 'hindajaid')
    return JsonResponse(list(soogikohad), safe=False)


def hindaEelroad1(request, soogikoha_id):
    soogikoht = get_object_or_404(models.Soogikohad, pk=soogikoha_id)
    soogikoht.eelroad += 1
    soogikoht.hindajaid += 1
    soogikoht.save()
    return render(request, 'index.html')


def hindaEelroad2(request, soogikoha_id):
    soogikoht = get_object_or_404(models.Soogikohad, pk=soogikoha_id)
    soogikoht.eelroad += 2
    soogikoht.hindajaid += 1
    soogikoht.save()
    return render(request, 'index.html')


def hindaEelroad3(request, soogikoha_id):
    soogikoht = get_object_or_404(models.Soogikohad, pk=soogikoha_id)
    soogikoht.eelroad += 3
    soogikoht.hindajaid += 1
    soogikoht.save()
    return render(request, 'index.html')


def hindaEelroad4(request, soogikoha_id):
    soogikoht = get_object_or_404(models.Soogikohad, pk=soogikoha_id)
    soogikoht.eelroad += 4
    soogikoht.hindajaid += 1
    soogikoht.save()
    return render(request, 'index.html')


def hindaEelroad5(request, soogikoha_id):
    soogikoht = get_object_or_404(models.Soogikohad, pk=soogikoha_id)
    soogikoht.eelroad += 5
    soogikoht.hindajaid += 1
    soogikoht.save()
    return render(request, 'index.html')


def hindasupid1(request, soogikoha_id):
    soogikoht = get_object_or_404(models.Soogikohad, pk=soogikoha_id)
    soogikoht.supid += 1
    soogikoht.hindajaid += 1
    soogikoht.save()
    return render(request, 'index.html')


def hindasupid2(request, soogikoha_id):
    soogikoht = get_object_or_404(models.Soogikohad, pk=soogikoha_id)
    soogikoht.supid += 2
    soogikoht.hindajaid += 1
    soogikoht.save()
    return render(request, 'index.html')


def hindasupid3(request, soogikoha_id):
    soogikoht = get_object_or_404(models.Soogikohad, pk=soogikoha_id)
    soogikoht.supid += 3
    soogikoht.hindajaid += 1
    soogikoht.save()
    return render(request, 'index.html')


def hindasupid4(request, soogikoha_id):
    soogikoht = get_object_or_404(models.Soogikohad, pk=soogikoha_id)
    soogikoht.supid += 4
    soogikoht.hindajaid += 1
    soogikoht.save()
    return render(request, 'index.html')


def hindasupid5(request, soogikoha_id):
    soogikoht = get_object_or_404(models.Soogikohad, pk=soogikoha_id)
    soogikoht.supid += 5
    soogikoht.hindajaid += 1
    soogikoht.save()
    return render(request, 'index.html')

def hindapraed1(request, soogikoha_id):
    soogikoht = get_object_or_404(models.Soogikohad, pk=soogikoha_id)
    soogikoht.supid += 1
    soogikoht.hindajaid += 1
    soogikoht.save()
    return render(request, 'index.html')


def hindapraed2(request, soogikoha_id):
    soogikoht = get_object_or_404(models.Soogikohad, pk=soogikoha_id)
    soogikoht.praed += 2
    soogikoht.hindajaid += 1
    soogikoht.save()
    return render(request, 'index.html')


def hindapraed3(request, soogikoha_id):
    soogikoht = get_object_or_404(models.Soogikohad, pk=soogikoha_id)
    soogikoht.praed += 3
    soogikoht.hindajaid += 1
    soogikoht.save()
    return render(request, 'index.html')


def hindapraed4(request, soogikoha_id):
    soogikoht = get_object_or_404(models.Soogikohad, pk=soogikoha_id)
    soogikoht.praed += 4
    soogikoht.hindajaid += 1
    soogikoht.save()
    return render(request, 'index.html')


def hindapraed5(request, soogikoha_id):
    soogikoht = get_object_or_404(models.Soogikohad, pk=soogikoha_id)
    soogikoht.praed += 5
    soogikoht.hindajaid += 1
    soogikoht.save()
    return render(request, 'index.html')

def hindamagus1(request, soogikoha_id):
    soogikoht = get_object_or_404(models.Soogikohad, pk=soogikoha_id)
    soogikoht.magustoidud += 1
    soogikoht.hindajaid += 1
    soogikoht.save()
    return render(request, 'index.html')


def hindamagus2(request, soogikoha_id):
    soogikoht = get_object_or_404(models.Soogikohad, pk=soogikoha_id)
    soogikoht.magustoidud += 2
    soogikoht.hindajaid += 1
    soogikoht.save()
    return render(request, 'index.html')


def hindamagus3(request, soogikoha_id):
    soogikoht = get_object_or_404(models.Soogikohad, pk=soogikoha_id)
    soogikoht.magustoidud += 3
    soogikoht.hindajaid += 1
    soogikoht.save()
    return render(request, 'index.html')


def hindamagus4(request, soogikoha_id):
    soogikoht = get_object_or_404(models.Soogikohad, pk=soogikoha_id)
    soogikoht.magustoidud += 4
    soogikoht.hindajaid += 1
    soogikoht.save()
    return render(request, 'index.html')


def hindamagus5(request, soogikoha_id):
    soogikoht = get_object_or_404(models.Soogikohad, pk=soogikoha_id)
    soogikoht.magustoidud += 5
    soogikoht.hindajaid += 1
    soogikoht.save()
    return render(request, 'index.html')

def hindajoogid1(request, soogikoha_id):
    soogikoht = get_object_or_404(models.Soogikohad, pk=soogikoha_id)
    soogikoht.joogid += 1
    soogikoht.hindajaid += 1
    soogikoht.save()
    return render(request, 'index.html')


def hindajoogid2(request, soogikoha_id):
    soogikoht = get_object_or_404(models.Soogikohad, pk=soogikoha_id)
    soogikoht.joogid += 2
    soogikoht.hindajaid += 1
    soogikoht.save()
    return render(request, 'index.html')


def hindajoogid3(request, soogikoha_id):
    soogikoht = get_object_or_404(models.Soogikohad, pk=soogikoha_id)
    soogikoht.joogid += 3
    soogikoht.hindajaid += 1
    soogikoht.save()
    return render(request, 'index.html')


def hindajoogid4(request, soogikoha_id):
    soogikoht = get_object_or_404(models.Soogikohad, pk=soogikoha_id)
    soogikoht.joogid += 4
    soogikoht.hindajaid += 1
    soogikoht.save()
    return render(request, 'index.html')


def hindajoogid5(request, soogikoha_id):
    soogikoht = get_object_or_404(models.Soogikohad, pk=soogikoha_id)
    soogikoht.joogid += 5
    soogikoht.hindajaid += 1
    soogikoht.save()
    return render(request, 'index.html')

def hindakohv1(request, soogikoha_id):
    soogikoht = get_object_or_404(models.Soogikohad, pk=soogikoha_id)
    soogikoht.kohvilaud += 1
    soogikoht.hindajaid += 1
    soogikoht.save()
    return render(request, 'index.html')


def hindakohv2(request, soogikoha_id):
    soogikoht = get_object_or_404(models.Soogikohad, pk=soogikoha_id)
    soogikoht.kohvilaud += 2
    soogikoht.hindajaid += 1
    soogikoht.save()
    return render(request, 'index.html')


def hindakohv3(request, soogikoha_id):
    soogikoht = get_object_or_404(models.Soogikohad, pk=soogikoha_id)
    soogikoht.kohvilaud += 3
    soogikoht.hindajaid += 1
    soogikoht.save()
    return render(request, 'index.html')


def hindakohv4(request, soogikoha_id):
    soogikoht = get_object_or_404(models.Soogikohad, pk=soogikoha_id)
    soogikoht.kohvilaud += 4
    soogikoht.hindajaid += 1
    soogikoht.save()
    return render(request, 'index.html')


def hindakohv5(request, soogikoha_id):
    soogikoht = get_object_or_404(models.Soogikohad, pk=soogikoha_id)
    soogikoht.kohvilaud += 5
    soogikoht.hindajaid += 1
    soogikoht.save()
    return render(request, 'index.html')