from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib.auth.mixins import UserPassesTestMixin
from ..models import Show, Booking

class IsAdminMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff

class ShowListView(IsAdminMixin, View):
    def get(self, request):
        shows = Show.objects.all()
        return render(request, 'admin/show_list.html', {'shows': shows})

class ShowCreateView(IsAdminMixin, View):
    def get(self, request):
        return render(request, 'admin/add_show.html')

    def post(self, request):
        Show.objects.create(
            name=request.POST['name'],
            date=request.POST['date'],
            venue=request.POST['venue'],
            total_seats=int(request.POST['total_seats']),
            available_seats=int(request.POST['total_seats']),
        )
        return redirect('show_list')

class ShowEditView(IsAdminMixin, View):
    def get(self, request, show_id):
        show = get_object_or_404(Show, id=show_id)
        return render(request, 'admin/edit_show.html', {'show': show})

    def post(self, request, show_id):
        show = get_object_or_404(Show, id=show_id)
        new_total = int(request.POST['total_seats'])
        diff = new_total - show.total_seats
        show.name = request.POST['name']
        show.date = request.POST['date']
        show.venue = request.POST['venue']
        show.total_seats = new_total
        show.available_seats += diff
        show.save()
        return redirect('show_list')

class ShowDeleteView(IsAdminMixin, View):
    def post(self, request, show_id):
        show = get_object_or_404(Show, id=show_id)
        show.delete()
        return redirect('show_list')

class AllBookingsView(IsAdminMixin, View):
    def get(self, request):
        bookings = Booking.objects.all()
        return render(request, 'admin/all_bookings.html', {'bookings': bookings})
