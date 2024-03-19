from django.shortcuts import render,redirect
from django.contrib import messages
from .models import CallReq, contactMsg, Intermship, Careers

# Create your views here.
def adminive(request):
    pass

def home(request):
    if request.method == 'POST':
        name=request.POST['name']
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        
        submit=CallReq.objects.create(name=name,email=email,phone=phone,description=desc).save()
        messages.success(request,"Send request succesful..")
        return redirect('/')
    return render(request,"home.html")

def contact(request):
    if request.method == 'POST':
        name=request.POST['namein']
        email=request.POST['emailin']
        phone=request.POST['noin']
        msg=request.POST['msg']

        submit=contactMsg.objects.create(name=name,email=email,phone=phone,message=msg).save()
        messages.success(request,"Submitted succesfully..")
        return redirect("contacts")
    
    return render(request,"contact.html")

def intern(request):
    if request.method == 'POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        course=request.POST['course']
        duration=request.POST['days']
        Intermship.objects.create(name=name,email=email,phone=phone,course=course,duration=duration).save()

        messages.success(request,"Submitted successfully..")
        return redirect('careerintern')

    return render(request,"carint.html")
        

def career(request):
    if request.method == 'POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        role=request.POST['carcho']
        file=request.FILES['files']

        Careers.objects.create(name=name,email=email,phone=phone,role=role,resume=file).save()
        messages.success(request,"Resume uploaded successfully..")
        return redirect('careerintern')


def service(request):
    return render(request,"services.html")