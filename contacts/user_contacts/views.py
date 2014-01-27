from django.shortcuts import (
    render,
    render_to_response)
from django.template import RequestContext
from django.http import HttpResponseRedirect

from user_contacts.models import (
    Phone,
    Person)
from user_contacts.new_contact_form import ContactForm


def home(request):
    return render_to_response('home.html')


def all_contacts(request):
    contacts = Phone.objects.all()
    return render_to_response('all.html', {'contacts': contacts})


def add_contact(request):
    person_form = ContactForm()
    return render(
        request,
        'add.html',
        {'person_form': person_form},
        context_instance=RequestContext(request))


def create(request):
    form = ContactForm(request.POST)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('all/')
    return render(
        request,
        'add.html',
        {'person_form': form},
        context_instance=RequestContext(request))
