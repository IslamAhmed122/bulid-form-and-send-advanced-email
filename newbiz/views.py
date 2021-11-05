
from django.core import mail
from django.shortcuts import redirect, render,get_object_or_404

from newbiz.models import *

from django.core.mail import message, send_mail
from django.conf import settings
# html email required stuff
from django.template.loader import render_to_string, get_template
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags

from project.settings import EMAIL_BACKEND
 
from .forms import CustomerForm
# Create your views here.
def home(request):
    web= newbiz.objects.last()
    About=Aboutus.objects.last()
    serv=Service.objects.all()
    choo=whychooseus.objects.all()
    
    team=Team.objects.all()[:6] 
    client=ourclients.objects.all()[:8]
    foot=footer.objects.all()
    contact=contactus.objects.all()
    image=imagelist.objects.all()[0:6]  

    context = {
        "web":web,
        "about":About,
        "service":serv,
        "chose":choo,
        
        "team":team,
        "client":client,
        "footer":foot,
        "contact":contact,
        "image":image,
        
    }

    



    return render(request,"hi.html",context)









def index(request):
    form=CustomerForm(request.POST or None)
    if request.method == 'POST':  
     form=CustomerForm(request.POST )
    if form.is_valid():
        print("thank you so much")
        print(form.cleaned_data)       
        Customer=form.save(commit=False)
        form.save()
        sendemail(request)
        return redirect("/")
    else:
        form=CustomerForm()  
    context={
        "form":form
    }

    return render(request,"index.html",context)
    

   
def sendemail(request):
    form=CustomerForm(request.POST or None)
    if request.method == 'POST': 
        name = request.POST['name']
        email = request.POST['email'] 
        subject = request.POST['subject'] 
        message = request.POST['message'] 
    
    subject = subject
    html_message = render_to_string('mail.html', {'name': name})
    plain_message = strip_tags(html_message)
    from_email = settings.EMAIL_HOST_USER
    to = email
    mail.send_mail(subject, plain_message, from_email, [to], html_message=html_message)
    context={
        "form":form
    }

    return render(request,"index.html",context)
    
        


    