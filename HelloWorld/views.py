from django.http import HttpResponse
from django.views.generic import TempleteView

def helloworldfunction(request):
  return HttpResponse('fdef')

class HelloworldClass(TempleteView):
  template_name = 'helloworld.html'