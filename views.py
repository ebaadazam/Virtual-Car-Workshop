from django.shortcuts import render, HttpResponse
# HttpResponse added manually

#imported manually
from datetime import datetime
from Myapp.models import Contact
from django.contrib import messages

# manually
def index(request):
    context = {
        'variable':"This is to test the variable thing"
    }
    return render(request, 'index.html', context)
    #return HttpResponse("Welcome to the E-Commerce website!")
 
def about(request):
    return render(request, 'about.html')
    #return HttpResponse("This is about page")

def services(request):
    return render(request, 'services.html')
    #return HttpResponse("This is a service page")
    
def drop1(request):
    return render(request, 'drop1.html')

def drop2(request):
    return render(request, 'drop2.html')

def drop3(request):
    return render(request, 'drop3.html')

def drop4(request):
    return render(request, 'drop4.html')

def contact(request):
    
    # Now we write the logic for adding the data from the website form to admin panel
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        service = request.POST.get('service')
        city = request.POST.get('city')
        state = request.POST.get('state')
        contact = Contact(name=name, email=email, number=number, service=service, city=city, state=state, date = datetime.today())
        contact.save()
        
        messages.success(request, "Your message has been sent")
    
    return render(request, 'contact.html')
    #return HttpResponse("This is a contact page")
