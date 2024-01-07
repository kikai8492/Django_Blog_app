
from django.contrib import admin
from django.urls import path
from .views import someview,HelloWorldClass

urlpatterns = [
	path('admin/', admin.site.urls),
  path('helloworld/',someview),
  path('helloworld2/', HelloWorldClass.as_view())
]
