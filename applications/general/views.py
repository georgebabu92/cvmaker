from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView


class GeneralDashboard(LoginRequiredMixin, TemplateView):
    login_url = 'accounts/login/'
    # redirect_field_name = ''
    template_name = 'base.html'