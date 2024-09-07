from django.shortcuts import render

from app.forms import ContactForm
from app.models import Contact, Project


def home_page(request):
    return render(request, "home.html")


def contact_page(request):
    context = {}

    if request.method == "POST":
        form = ContactForm(data=request.POST)

        if form.is_valid():
            form.save()
            context["success"] = True
            context["error"] = False
        else:
            context["success"] = False
            context["error"] = True
    else:
        form = ContactForm

    context["form"] = form

    return render(request, "contact.html", context=context)


def project_list_page(request):
    projects = Project.objects.all()

    return render(request, "project-list.html", {"projects": projects})


def project_detail_page(request, pk):
    project = Project.objects.get(pk=pk)

    return render(request, "project-detail.html", {"project": project})


def inquiry_list_page(request):
    inquiries = Contact.objects.all()

    return render(request, "inquiry-list.html", {"inquiries": inquiries})
