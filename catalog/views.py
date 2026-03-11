from django.contrib.auth.mixins import (  # Добавлен миксин проверки условий
    LoginRequiredMixin, UserPassesTestMixin)
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  TemplateView, UpdateView)

from catalog.forms import ProductForm
from catalog.models import Product


class ProductListView(ListView):
    model = Product
    template_name = "catalog/index.html"


class ProductDetailView(DetailView):
    model = Product
    template_name = "catalog/product_detail.html"


class ContactTemplateView(TemplateView):
    template_name = "catalog/contacts.html"


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy("catalog:home")

    def form_valid(self, form):
        """Автоматически назначает текущего пользователя владельцем продукта."""
        product = form.save(commit=False)
        product.owner = self.request.user
        product.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy("catalog:home")

    def test_func(self):
        """Проверяет, что редактировать может только владелец."""
        return self.request.user == self.get_object().owner


class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    template_name = "catalog/product_confirm_delete.html"
    success_url = reverse_lazy("catalog:home")

    def test_func(self):
        """Удалять может владелец или модератор с соответствующим правом."""
        user = self.request.user
        obj = self.get_object()

        return user == obj.owner or user.has_perm("catalog.delete_product")
