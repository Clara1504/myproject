
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('sobre/', TemplateView.as_view(template_name='sobre.html'), name='sobre'),
    path('doacoes/', TemplateView.as_view(template_name='doacoes.html'), name='doacoes'),
    path('adocao/', TemplateView.as_view(template_name='adocao.html'), name='adocao'),
]