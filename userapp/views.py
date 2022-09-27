from django.shortcuts import render, redirect
from userapp.models import usermodel

# Create your views here.
def loginview(request):
    if request.method == 'POST':
        userData = usermodel.objects.get(email=request.POST['email'])
        if userData.password==request.POST['password']:
            request.session['userId'] = userData.id
            return redirect('home')
    return render(request,'login.html')

def signupview(request):
    if request.method=='POST':
        model = usermodel()
        model.name = request.POST['name']
        model.email = request.POST['email']
        model.contact = request.POST['number']
        model.password = request.POST['password']
        model.save()
        return redirect('home')
    return render(request,'signup.html')