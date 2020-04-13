from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
                            CreateView,
                            DeleteView,
                            DetailView,
                            ListView,
                            UpdateView
)
from .models import Product
from .forms import ProductModelForm
from django.urls import reverse

class ProductListView(LoginRequiredMixin, ListView):
    model = Product

class ProductCreateView(LoginRequiredMixin, CreateView):
    template_name = 'product/product_create.html'
    form_class = ProductModelForm
    model = Product
    def get_success_url(self):
        return reverse('product:product-list')

class ProductDetailView(LoginRequiredMixin, DetailView):
    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Product, id=id_)

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        ppp = kwargs.get('object', None)
        sell_product_list = ppp.product_sells.all()
        proj_product_list = ppp.product_projects.all()
        if sell_product_list or proj_product_list:
            context.update({'sell_product_list': sell_product_list, 'proj_product_list': proj_product_list})
        return context


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'product/product_create.html'
    form_class = ProductModelForm
    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Product, id=id_)
    def get_success_url(self):
        return reverse('product:product-list')

class ProductDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'product/product_delete.html'
    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Product, id=id_)
    def get_success_url(self):
        return reverse('product:product-list')
