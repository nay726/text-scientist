

from django.contrib import admin
from django.urls import path
from.import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.start,name='start'),
    path('analyze', views.analyze,name='analyze'),

]
