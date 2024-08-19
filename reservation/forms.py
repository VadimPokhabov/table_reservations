from django import forms

from common.view import StyleFormMixin
from reservation.models import Table, Reservation
from users.models import User


class TableForms(StyleFormMixin, forms.ModelForm):
    def __init__(self, *args, request=None, **kwargs):
        super().__init__(*args, **kwargs)
        if request is not None:
            self.fields['recipients'].queryset = User.objects.filter(owner=request.user)
            self.fields['table'].queryset = Table.objects.filter(owner=request.user)

    class Meta:
        model = Table
        fields = ('table', 'seats')


class ReservationForm(StyleFormMixin, forms.ModelForm):
    # time_reserved = forms.CharField(
    #     widget=forms.TextInput(attrs={'class': 'input-group'}))
    # date_reserved = forms.DateField(widget=forms.TextInput(
    #     attrs={'placeholder': 'yyyy-mm-dd',
    #            'id': 'datepicker'}), required=True,)

    class Meta:
        model = Reservation
        fields = ['first_name',
                  'email', 'time_reserved',
                  'date_reserved']


class ReservationUpdateForm(StyleFormMixin, forms.ModelForm):
    # time_reserved = forms.CharField(
    #     widget=forms.TextInput(attrs={'id': 'timepicker',
    #                                   'class': 'input-group'}))
    # date_reserved = forms.DateField(widget=forms.TextInput(
    #     attrs={'placeholder': 'yyyy-mm-dd',
    #            'id': 'datepicker'}), required=True,)

    class Meta:
        model = Reservation
        fields = ['first_name',
                  'email', 'time_reserved',
                  'date_reserved']
