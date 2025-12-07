from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path("pricing/", views.pricing, name="pricing"),
    path("contact/", views.contact, name="contact"),
    path("terms/", views.terms, name="terms"),
    path("privacy/", views.privacy, name="privacy"),
    path("refunds/", views.refund, name="refund"),
    path("shipping/", views.shipping, name="shipping"),
]
