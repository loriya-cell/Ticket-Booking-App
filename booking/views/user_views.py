from django.shortcuts import redirect, render, get_object_or_404
from django.views import View
from booking.models import Show, Booking
from django.http import Http404


class HomeView(View):
    def get(self, request):
        shows = Show.objects.all()
        return render(request, 'user/home.html', {'shows': shows})

class BookTicketView(View):
    def get(self, request, show_id):
        try:
            show = Show.objects.get(id=show_id)
        except Show.DoesNotExist:
            raise Http404("Show not found")
        return render(request, 'user/book_ticket.html', {'show': show})
    
    def post(self, request, show_id):
        # Fetch the show by ID or return 404 if not found
        show = get_object_or_404(Show, id=show_id)
        booked_seats = int(request.POST['seats'])

        # Check if there are enough available seats
        if booked_seats <= show.available_seats:
            # Create a booking
            booking = Booking(user=request.user, show=show, seats=booked_seats)
            booking.save()

            # Update available seats for the show
            show.available_seats -= booked_seats
            show.save()

            # Redirect to booking history or success page
            return redirect('booking_history')
        else:
            # Return with error message if not enough seats are available
            return render(request, 'user/book_ticket.html', {'show': show, 'error': 'Not enough available seats'})

class BookingHistoryView(View):
    def get(self, request):
        bookings = Booking.objects.filter(user=request.user)
        return render(request, 'user/booking_history.html', {'bookings': bookings})
