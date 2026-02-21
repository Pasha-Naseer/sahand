from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'hotel'
urlpatterns = [
    path('', views.index, name='index'),
    path('room/<int:room_id>/', views.DetailView.as_view(), name='detail'),
    path('room/<int:room_id>/reservation/', views.ReservationView.as_view(), name='reservation'),
    path('room/<int:room_id>/reservation_success/', views.ReservationSuccessView.as_view(), name='reservation_success'),
    path('status/', views.ReservationStatus.as_view(), name='reservation_status'),
    path('about/', views.about, name='about'),
    path("login/", views.UserLoginView.as_view(), name='login'),
    path("logout/", views.user_logout, name='logout'),
    path('register/', views.UserRegisterView.as_view(), name='register'),
    path('verify/', views.UserRegisterVerifyCodeView.as_view(), name='verify_code'),
    path('update/', views.user_update, name='update'),
    # path('update_info/', views.update_info, name='update_info'),
    path('update_password', views.update_password, name='update_password'),
    path('weblog', views.weblog, name='weblog'),
    path('weblog/<int:weblog_id>/', views.weblog_detail, name='weblog_detail'),
    path('checkout/', views.CheckoutView.as_view(), name='checkout'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
