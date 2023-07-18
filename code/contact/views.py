from django.shortcuts import render, redirect  
from contact.forms import ContactForm  
from contact.models import Contact 

# Create your views here.  
def create(request):  
    if request.method == "POST":  
        form = ContactForm(request.POST)  
        # if form.is_valid():  
        try:  
            form.save()  
            return redirect('/show')  
        except:  
            pass  
    else:  
        form = ContactForm()  
    return render(request,'index.html',{'form':form})  
def show(request):  
    contacts = Contact.objects.all()  
    return render(request,"show.html",{'contacts':contacts})  
def edit(request, id):  
    contact = Contact.objects.get(id=id)  
    return render(request,'edit.html', {'contact':contact})  
def update(request, id):  
    contact = Contact.objects.get(id=id)  
    form = ContactForm(request.POST, instance = contact)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'contact': contact})  
def destroy(request, id):  
    contact = Contact.objects.get(id=id)  
    contact.delete()  
    return redirect("/show")  
