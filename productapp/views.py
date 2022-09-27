from django.shortcuts import render, redirect

from productapp.models import categorymodel, productmodel

# Create your views here.
def homeview(request):
    if 'userId' in request.session.keys():
        categoryData = categorymodel.objects.all()
        return render(request,'home.html',{'categoryKey':categoryData})
    else:
        return redirect('login')

def productview(request):
    if 'userId' in request.session.keys():
        productData = productmodel.objects.all()
        return render(request,'product.html',{'productData':productData})
    else:
        return redirect('login')

def logoutview(request):
    #return render(request,'login.html')
    del request.session['userId']
    return redirect('login')