from django.urls import path
from . import views

urlpatterns = [
    # path('robo/', views.robotData.as_view()),
    path('robotdata/<status>/',views.getrobotData.as_view()),
    path('getroboData/<id>/<status>/', views.getrobotDataStatus.as_view()),

    #new

]
