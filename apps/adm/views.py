from django.shortcuts import render
from django.views.generic.base import View

from utils.mixin_utils import LoginRequiredMixin


class AdmView(LoginRequiredMixin, View):

    def get(self, request):
        return render(request, 'adm/adm_index.html')
