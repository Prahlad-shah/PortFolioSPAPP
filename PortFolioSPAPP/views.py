from django.shortcuts import render

# Create your views here.

class PortFolioSPA():
    
    def indexPage(request):
        return render(request, 'index.html')