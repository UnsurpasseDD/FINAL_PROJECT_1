import django_filters
import pytz
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from django.views.decorators.cache import cache_page

#from .forms import PostForm
from .models import Post, Category
from django.http import HttpResponse
from django.views import View
#from .tasks import hello, shared_task, printer
from django.core.cache import cache
from django.utils.translation import gettext as _
from django.utils import timezone



# Create your views here.


class NewsList(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'posts'
    ordering = '-time_in'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_author'] = not self.request.user.groups.filter(name='authors').exists()
        context['current_time'] = timezone.now()
        return context