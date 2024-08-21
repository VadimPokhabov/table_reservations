from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView, DeleteView

from reservation.forms import TableForms, ReservationForm, ReservationUpdateForm
from reservation.models import Table, Reservation
from reservation.users_cases import save_feedback


class TableTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'reservation/home.html'


class TableCreateView(LoginRequiredMixin, CreateView):
    model = Table
    form_class = TableForms
    success_url = reverse_lazy('reservation:table_list')

    def form_valid(self, form):
        message = form.save()
        message.owner = self.request.user
        message.save()
        return super().form_valid(form)


class TableListView(LoginRequiredMixin, ListView):
    model = Table


class TableDetailView(LoginRequiredMixin, DetailView):
    model = Table


class TableUpdateView(LoginRequiredMixin, UpdateView):
    model = Table
    form_class = TableForms
    success_url = reverse_lazy('reservation:table_list')


class TableDeleteView(LoginRequiredMixin, DeleteView):
    model = Table
    success_url = reverse_lazy('reservation:table_list')


class ReservationListView(ListView):
    model = Reservation
    title = 'Бронирование'

    def get_queryset(self, args, **kwargs):
        """
        Отображает только доступные к брони столики.
        """
        queryset = super().get_queryset(args, **kwargs)
        queryset = queryset.filter(is_booked=False)
        return queryset


class ReservationCreateView(LoginRequiredMixin, CreateView):
    model = Reservation
    template_name = "reservation/reservation.html"
    form_class = ReservationForm
    success_url = reverse_lazy('reservation:reservation')

    def form_valid(self, form):
        new_reservate = form.save(commit=False)
        new_reservate.owner = self.request.user
        new_reservate.save()
        super().form_valid(form)
        return redirect('/')
        # send a flash message to the user
        # messages.success(
        #     self.request,
        #     "Вы успешно забронировали новый столик ")
        # redirect the user back to his/her dashboard


class AboutRestoTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'reservation/about_restaurant.html'


class UpdateReservation(LoginRequiredMixin, UpdateView):
    """Admin user updates all the reservation."""
    form_class = ReservationUpdateForm
    template_name = "super/update_reserve.html"
    model = Reservation

    def get_object(self, *args, **kwargs):
        obj = get_object_or_404(Reservation, pk=self.kwargs['pk'])
        return obj

    def form_valid(self, form):
        val = form.cleaned_data['status']
        form.save()
        messages.success(
            self.request, "you have successfully updated the reservation")
        if val == "confirmed":
            return redirect('orders:reservation_status', pk=self.kwargs['pk'])
        return redirect('/dashboard')


class ContactsTemplateView(TemplateView):
    template_name = "reservation/contacts.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Контакты"
        return context

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            save_feedback(
                name=request.POST.get('name'),
                phone=request.POST.get('phone'),
                message=request.POST.get('message')
            )
        return HttpResponseRedirect(reverse('reservation:contacts'))
