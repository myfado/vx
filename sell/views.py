from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.db import transaction

class SellList(LoginRequiredMixin, ListView):
    model = Sell

class SellDetail(LoginRequiredMixin, DetailView):
    model = Sell

    def get_context_data(self, **kwargs):
        context = super(SellDetail, self).get_context_data(**kwargs)
        sell_item = kwargs.get('object', None)
        sell_object_list = sell_item.has_items.all()

        if sell_object_list:
            context.update({'sell_object_list': sell_object_list})
        return context

class SellItemList(LoginRequiredMixin, ListView):
    model = SellItem
    template_name = 'sell/sell_active.html'

    def get_context_data(self, **kwargs):
        context = super(SellItemList, self).get_context_data(**kwargs)
        active_list = SellItem.objects.filter(discontinued=False)
        context['active_list'] = active_list
        return context

class SellCreate(LoginRequiredMixin, CreateView):
    model = Sell
    template_name = 'sell/sell_create.html'
    form_class = SellForm
    success_url = None

    def get_context_data(self, **kwargs):
        data = super(SellCreate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['items'] = SellItemFormSet(self.request.POST)
        else:
            data['items'] = SellItemFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        items = context['items']
        with transaction.atomic():
            self.object = form.save()

            if items.is_valid():
                items.instance = self.object
                items.save()
        return super(SellCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('sell:sell-detail', kwargs={'pk': self.object.pk})

class SellUpdate(LoginRequiredMixin, UpdateView):
    model = Sell
    template_name = 'sell/sell_create.html'
    form_class = SellForm
    success_url = None

    def get_context_data(self, **kwargs):
        data = super(SellUpdate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['items'] = SellItemFormSet(self.request.POST, instance=self.object)
        else:
            data['items'] = SellItemFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        items = context['items']
        with transaction.atomic():
            self.object = form.save()

            if items.is_valid():
                items.instance = self.object
                items.save()
        return super(SellUpdate, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('sell:sell-detail', kwargs={'pk': self.object.pk})


class SellDelete(LoginRequiredMixin, DeleteView):
    model = Sell
    template_name = 'sell/sell_delete.html'
    success_url = reverse_lazy('sell:sell-list')
