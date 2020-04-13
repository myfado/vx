from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.db import transaction

class PurchaseList(LoginRequiredMixin, ListView):
    model = Purchase

class PurchaseDetail(LoginRequiredMixin, DetailView):
    model = Purchase

    def get_context_data(self, **kwargs):
        context = super(PurchaseDetail, self).get_context_data(**kwargs)
        purchase_item = kwargs.get('object', None)
        purchase_object_list = purchase_item.what_is_going.all()
        if purchase_object_list:
            context.update({'purchase_object_list': purchase_object_list})
        return context

class PurchaseCreate(LoginRequiredMixin, CreateView):
    model = Purchase
    template_name = 'purchase/purchase_create.html'
    form_class = PurchaseForm
    success_url = None

    def get_context_data(self, **kwargs):
        data = super(PurchaseCreate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['items'] = PurchaseItemFormSet(self.request.POST)
        else:
            data['items'] = PurchaseItemFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        items = context['items']
        with transaction.atomic():
            self.object = form.save()

            if items.is_valid():
                items.instance = self.object
                items.save()
        return super(PurchaseCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('purchase:purchase-detail', kwargs={'pk': self.object.pk})

class PurchaseUpdate(LoginRequiredMixin, UpdateView):
    model = Purchase
    template_name = 'purchase/purchase_create.html'
    form_class = PurchaseForm
    success_url = None

    def get_context_data(self, **kwargs):
        data = super(PurchaseUpdate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['items'] = PurchaseItemFormSet(self.request.POST, instance=self.object)
        else:
            data['items'] = PurchaseItemFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        items = context['items']
        with transaction.atomic():
            self.object = form.save()

            if items.is_valid():
                items.instance = self.object
                items.save()
        return super(PurchaseUpdate, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('purchase:purchase-detail', kwargs={'pk': self.object.pk})


class PurchaseDelete(LoginRequiredMixin, DeleteView):
    model = Purchase
    template_name = 'purchase/purchase_delete.html'
    success_url = reverse_lazy('purchase:purchase-list')
