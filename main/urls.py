from django.urls import path, re_path

from main import views

urlpatterns = [
    # path('', views.hello),
    re_path('(.)*', views.hello),
    # re_path("(?P<key>(.)*)/",views.test),
]


# /g3egns3yk2ahzb0p&location=shenzhen&language=en
