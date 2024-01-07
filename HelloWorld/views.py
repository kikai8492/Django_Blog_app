from django.http import HttpResponse
from django.views.generic import TemplateView
# from pathlib import Path

# def helloworldfunction(request):
#   return HttpResponse('fdef')

class HelloWorldClass(TemplateView):
  template_name = 'hello.html'

def someview(request):
  print(Path(__file__).resolve().parent.parent)
  return HttpResponse('fwaefa')