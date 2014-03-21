import random
from django.shortcuts import render
from pocket.models import Pocket


def index(request):
    Pocket.objects.all().delete()
    for n in range(0,9):
        a = Pocket.objects.create_pocket(str(random.randint(0,9)))
        a.save()
    return render(request, "index.html", {"number": Pocket.objects.all()})


def cycle(request):
    boo = []
    for number in Pocket.objects.all():
        boo.append(number.number)
        a=boo[:3]
        b=boo[3:6]
        c=boo[-3:]
    one = a[:-1]
    one.insert(0, b[0])
    two = [c[0], b[1], a[2]]
    three = c[1:]
    three.append(b[2])
    numbers = one+two+three
    Pocket.objects.all().delete()
    for n in numbers:
        a = Pocket.objects.create_pocket(n)
        a.save()
    return render(request, "index.html", {"number": Pocket.objects.all()})



