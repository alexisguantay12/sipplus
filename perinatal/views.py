#from django.http import request
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, ListView, UpdateView

from .forms import *
from .models import *

from .gx_auth import show_cookie_view


class ListPerinatalView(ListView):
    # model = None
    # context_object_name = 'test'
    # queryset = []
    # template_name = 'index.html'
    pass

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CreatePerinatalView(CreateView):

    template_name = 'new-registry-copy.html'
    form_class = HcpHcPerinatalForm
    model = HcpHcPerinatal
    success_url = reverse_lazy('create_perinatal_record')

    def get(self, request, *args, **kwargs):
        # Accede al objeto request aquí
        cookie_data = show_cookie_view(request)
        print(cookie_data)
        return super().get(request, *args, **kwargs)

class UpdatePerinatalView(UpdateView):
    template_name = 'new-registry-copy.html'
    form_class = HcpHcPerinatalForm
    model = HcpHcPerinatal
    success_url = reverse_lazy('create_perinatal_record')
    

class DetailPerinatalView(View):
    pass


class PreviewPerinatalPDFView(View):
    pass


class DownloadPerinatalPDFView(View):
    pass


# def test(request):
#     context = {
#         'form': TestForm(),
#     }
#     return render(request, 'test.html', context)
