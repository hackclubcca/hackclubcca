from django.shortcuts import render
from HackClubCCA.forms import EmailForm
from airtable import Airtable
from validate_email import validate_email
import os

airtable = Airtable(api_key=os.environ.get("KEY"), table_name='emails', base_key=os.environ.get("BASE_KEY"))


def index(request):
    form = EmailForm()
    if request.method == "POST":
        form = EmailForm(request.POST)
        if form.is_valid() and validate_email(form.cleaned_data["email"],verify=True):
            airtable.insert({
                "email": form.cleaned_data["email"],
                "latitude": request.GET.get("latitude", 0),
                "longitude": request.GET.get("longitude", 0)
            })
            return render(request, "index.html", context={
                "submitted": True
            })
        else:
            return render(request, "index.html", context={
                "submitted": True,
                "message": "Oops... that's not a valid email",
            })
    return render(request, "index.html", context={
        "form": form
    })