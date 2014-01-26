from django.shortcuts import (
    render,
    render_to_response)


def home(request):
    return render_to_response('home.html')


def all_contacts(request):
    contacts = Phone.objects.all()
    return render_to_response('all.html', {'contacts': contacts})
