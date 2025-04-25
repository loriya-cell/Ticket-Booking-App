from django.contrib import admin
from django.urls import path
from booking.views import HomeView, LoginView, RegisterView, LogoutView, BookTicketView, BookingHistoryView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Auth routes (login, register, logout)
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    
    # User routes (home, book ticket, booking history)
    path('home/', HomeView.as_view(), name='home'),
    path('book_ticket/<int:show_id>/', BookTicketView.as_view(), name='book_ticket'),
    path('booking_history/', BookingHistoryView.as_view(), name='booking_history'),
    
    # Optionally, you can use the root URL as the homepage as well
    path('', HomeView.as_view(), name='home'),
]