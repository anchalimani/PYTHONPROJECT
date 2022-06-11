from django.urls import path
from .import views

urlpatterns = [
    path('hi/',views.hello),
    path('home/',views.stud),
    path('1/',views.fun),
    path('2/',views.new),
    path('3/',views.web),
    path('4/',views.base),
    path('up/',views.update),
    path('dele/',views.dele),
    path('mail/',views.mail),
    path('message/',views.message),
    path('email/', views.email),

]