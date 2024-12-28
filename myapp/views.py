from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    projects=Projects.objects.all()
    educations=Education.objects.all()
    tskills=Techskills.objects.all()
    sskills=Softskills.objects.all()
    contacts=Contacts.objects.all()

    return render(request,'index.html',{'projects':projects,'educations':educations,'tskills':tskills,'sskills':sskills,'contacts':contacts})

def feedback(request):
    if request.method=='POST':
        name=request.POST['uname']
        email=request.POST['email']
        msg=request.POST.get('msg')
        if name and email and msg: 
          Feedback.objects.create(name=name,email=email,msg=msg)
          return render(request,'feedback.html')
    return redirect('/')
    