from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
# previous login view
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    ##password change urls
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    ##password reset urls
    path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
    path('users/',views.UserListView.as_view(),name='user'),
    path('user-edit/<int:pk>',views.UserDeleteView.as_view(),name='user_r&d'),
    path('organizers/',views.EventListView.as_view(),name='organizers'),
    path('organizers-edit/<int:pk>',views.EventDeleteView.as_view(),name='edit')

]