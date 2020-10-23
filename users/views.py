from urllib import request
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views import generic
from .forms import *
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect


# Create your views here.
def base(request):
    return render(request, 'templates/base.html',
                  {'Calorie Tracker': base})


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'




