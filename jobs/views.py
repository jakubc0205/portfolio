from django.shortcuts import render


def home(request):
    return render(request, "jobs/home.html")


def jobs(request):
    return render(request, "jobs/jobs.html")


def contact(request):
    return render(request, "jobs/contact.html")


def skills(request):
    return render(request, "jobs/skills.html")


def hobbies(request):
    return render(request, "jobs/hobbies.html")
