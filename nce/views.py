from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    ListView, DetailView,
    TemplateView)
from .models import Project, Department
from .forms import ContactForm
from django.contrib import messages




class Home(ListView):
    model = Project
    template_name = 'landingpage.html'


def department(request, departments):
    project = Project.objects.filter(
        departments__name__contains= department
    ).order_by(
        'title'
    )
    context = {
        "department": department,
        'project': project
    }
    return render(request, 'nceprojectsite/departments.html', context)


class ListOfProject(ListView):
    model = Project
    template_name = 'nceprojectsite/projectlist.html'


class ProjectDetailView(DetailView):
    model = Project
    context_object_name = 'project'
    template_name = 'nceprojectsite/detail.html'


class HireWriter(TemplateView):
	template_name = 'nceprojectsite/hire.html'


class Services(TemplateView):
    template_name = 'services.html'


class Payment(TemplateView):
    template_name = 'nceprojectsite/payment.html'


class About(TemplateView):
    template_name = 'about.html'


def contact(request):
    if request.method =='POST':
        f = ContactForm(request.POST)
        if f.is_valid():
            f.save()
            messages.add_message(request, messages.INFO,'Thanks for contacting us. we will get back to you soon!')
            return redirect('feedback')
    else:
        f = ContactForm()
    return render(request, 'contact.html', {'form': f})