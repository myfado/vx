from django import forms
from .models import *
from django.forms.models import inlineformset_factory
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Fieldset, Div, HTML, ButtonHolder, Submit
from .custom_layout_object import *

class PurchaseForm(forms.ModelForm):

    class Meta:
        model = Purchase
        exclude = ()

    def __init__(self, *args, **kwargs):
        super(PurchaseForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3 create-label'
        self.helper.field_class = 'col-md-9'
        self.helper.layout = Layout(
            Div(
                Field('application'),
                Field('front_partner'),
                Field('product'),
                Field('quantity'),
                Field('back_partner'),
                Field('structure'),
                Field('replacing'),
                Field('price'),
                Fieldset('Add items',
                    Formset('items')),
                Field('deadline'),
                Field('discontinued'),
                Field('RND'),
                Field('completed'),
                HTML("<br>"),
                ButtonHolder(Submit('submit', 'save')),
                )
            )


class PurchaseItemForm(forms.ModelForm):

    class Meta:
        model = PurchaseItem
        exclude = ()

PurchaseItemFormSet = inlineformset_factory(
    Purchase, PurchaseItem, form=PurchaseItemForm,
    fields=['purchase', 'stage', 'comment'], extra=4
    )
