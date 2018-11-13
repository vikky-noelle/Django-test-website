from django.urls import path, re_path

from. import views

urlpatterns=[
    path("", views.index, name='home'),
    re_path(r'^blog/$', views.blog, name='blog'),
    re_path(r'^about/$', views.about, name='about'),
    re_path(r'^ajax/validate_your_email/$', views.validate_your_email, name='validate_your_email'),
]
