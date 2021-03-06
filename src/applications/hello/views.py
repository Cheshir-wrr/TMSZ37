from django import forms
from django.views.generic import FormView
from django.views.generic import RedirectView


class HelloForm(forms.Form):
    name = forms.CharField()
    address = forms.CharField()
    book = forms.CharField()


class HelloView(FormView):
    form_class = HelloForm
    success_url = "/h/"
    template_name = "hello/hello.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        name = self.request.session.get("name")
        address = self.request.session.get("address")
        book = self.request.session.get("book")

        context.update(
            {
                "address": address or "nowhere",
                "name": name or "anonymous",
                "book": book or "poof",
            }
        )

        return context

    def form_valid(self, form):
        name = form.cleaned_data["name"]
        address = form.cleaned_data["address"]
        book = form.cleaned_data["book"]
        self.request.session["name"] = name
        self.request.session["address"] = address
        self.request.session["book"] = book
        return super().form_valid(form)


class HelloResetView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        self.request.session.clear()
        return "/h/"
