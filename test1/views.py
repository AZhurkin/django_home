from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse


# Create your views here.

class Test1View(View):

    def get(self, request):
        return render(request, 'page1/index.html')

    def post(self, request):
        html = "<html><body>"
        for k, v in request.POST.items():
            html += f"{k}: {v}<br>"
        html += "</body></html>"
        return HttpResponse(html)


class PageTwo(View):

    def get(self, request):
        return render(request, 'page2/index.html')

    def post(self, request):
        html = "<html><body>"
        for i in request.POST.items():
            html += f"{i}<br>"
        html += "</body></html>"
        return HttpResponse(html)
        
class ContactView(View):

    def get(self, request):
        return render(request, 'test1/contact.html')

    def post(self, request):
        html = "<html><body>"
        for i in request.POST.items():
            html += f"{i}<br>"
        html += "</body></html>"
        return HttpResponse(html) 
