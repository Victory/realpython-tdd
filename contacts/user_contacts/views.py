from django.shortcuts import (
    render,
    render_to_response)
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import DetailView

from user_contacts.models import (
    Phone,
    Person)
from user_contacts.new_contact_form import ContactForm


def home(request):
    return render_to_response('home.html')


class DetailContactView(DetailView):
    model = Person
    template_name = 'contact.html'

def validate(request):
    post = request.POST
    field_name = post['field_name']
    field_value = post['field_value']
    data_for_form = {}
    data_for_form[field_name] = field_value

    form = ContactForm(data_for_form)
    field = form.fields[field_name]
    data = field.widget.value_from_datadict(
        form.data, form.files, form.add_prefix(field_name))
    cleaned_data = field.clean(data)
    if data == cleaned_data:
        result = "valid"
    else:
        result ="error"

    data = '{"result":"' + result + '"}'
    return HttpResponse(data, content_type="text/json")


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
