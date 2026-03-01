from django.views.generic import ListView, DetailView, TemplateView
from catalog.models import Product

class ProductListView(ListView):
    model = Product
    template_name = 'catalog/index.html'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'

class ContactTemplateView(TemplateView):
    template_name = 'catalog/contacts.html'