from django.urls import include, path
from . import views

urlpatterns = [
  path('bedlists', views.bed_list),
  path('bookbed', views.bed_booking),
  path('reschedulebook/<int:bed_id>', views.reschedule_book),
  path('cancelbook/<int:bed_id>', views.cancel_book)
]