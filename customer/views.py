from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
                            CreateView,
                            DeleteView,
                            DetailView,
                            ListView,
                            UpdateView
)
from .forms import CustomerModelForm
from .models import Customer
from sell.models import *

class CustomerList(LoginRequiredMixin, ListView):
    model = Customer

class CustomerDetail(LoginRequiredMixin, DetailView):
    model = Customer

    def get_context_data(self, **kwargs):
        context = super(CustomerDetail, self).get_context_data(**kwargs)
        customer = kwargs.get('object', None)
        converter_sales = customer.converter_sales.all()
        prods = SellItem.objects.filter(sell_id__in=converter_sales)
        proj_product_list = customer.front_partner_projects.all()
        if prods or proj_product_list:
            context.update({'prods': prods, 'proj_product_list': proj_product_list})
        return context


class CustomerCreate(LoginRequiredMixin, CreateView):
    template_name = 'customer/customer_create.html'
    form_class = CustomerModelForm

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('customer:customer-list')

class CustomerUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'customer/customer_create.html'
    form_class = CustomerModelForm

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Customer, id=id_)

    def get_success_url(self):
        return reverse('customer:customer-list')


class CustomerDelete(LoginRequiredMixin, DeleteView):
    model = Customer
    template_name = 'customer/customer_delete.html'
    success_url = reverse_lazy('customer:customer-list')
