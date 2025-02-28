from django.urls import path

from . import views


urlpatterns = [
    path('bye/<int:pk>/', views.GetStripeSessionId.as_view(),
         name='get_session_id'),
    path('item/<int:pk>/', views.ItemDetailView.as_view(), name='item'),
    path("success/", views.SuccessView.as_view(), name="success"),
    path("cancel/", views.CancelView.as_view(), name="cancel"),
    path('order/<int:pk>/', views.get_order, name='order'),
]
