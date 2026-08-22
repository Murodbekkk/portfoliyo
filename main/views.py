from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods

from .forms import ContactForm
from .models import Skill, Project, Experience, Profile


def index(request):
    profile = Profile.load()
    skills = Skill.objects.all()
    projects = Project.objects.all()
    experiences = Experience.objects.all()

    skills_by_category = {}
    for skill in skills:
        skills_by_category.setdefault(skill.get_category_display(), []).append(skill)

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Xabaringiz muvaffaqiyatli yuborildi. Tez orada javob beraman!")
            return redirect("main:index")
    else:
        form = ContactForm()

    context = {
        "profile": profile,
        "skills_by_category": skills_by_category,
        "projects": projects,
        "featured_projects": projects.filter(featured=True),
        "experiences": experiences,
        "form": form,
    }
    return render(request, "main/index.html", context)


def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    related = Project.objects.exclude(pk=project.pk)[:3]
    return render(request, "main/project_detail.html", {
        "project": project,
        "related": related,
        "profile": Profile.load(),
    })
