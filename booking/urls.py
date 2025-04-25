from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('home/', views.HomeView.as_view(), name='home'),
    path('book_ticket/<int:show_id>/', views.BookTicketView.as_view(), name='book_ticket'),
    path('booking_history/', views.BookingHistoryView.as_view(), name='booking_history'),
    path('admin/shows/', views.ShowListView.as_view(), name='show_list'),
    path('admin/shows/add/', views.ShowCreateView.as_view(), name='add_show'),
    path('admin/shows/edit/<int:show_id>/', views.ShowEditView.as_view(), name='edit_show'),
    path('admin/shows/delete/<int:show_id>/', views.ShowDeleteView.as_view(), name='delete_show'),
    path('admin/bookings/', views.AllBookingsView.as_view(), name='all_bookings'),
]
