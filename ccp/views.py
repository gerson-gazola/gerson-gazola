from imaplib import _Authenticator
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .forms import CrudForm
from .models import CrudModel

# Create your views here.
def login(request):
    return render(request, 'login.html', {})
    
def indexView(request):
    data =  CrudModel.objects.all()
    context = { 'employees': data }   
    return render(request, 'index.html', context)

def formularioParte1(request): 
    data =  CrudModel.objects.all()
    context = { 'employees': data }   
    return render(request, 'formulario1.html', context)    

def formularioParte2(request): 
    data =  CrudModel.objects.all()
    context = { 'employees': data }   
    return render(request, 'formulario2.html', context)

def formularioParte3(request): 
    data =  CrudModel.objects.all()
    context = { 'employees': data }   
    return render(request, 'formulario3.html', context)

def formularioParte4(request): 
    data =  CrudModel.objects.all()
    context = { 'employees': data }   
    return render(request, 'formulario4.html', context)  

def formularioParte5(request): 
    data =  CrudModel.objects.all()
    context = { 'employees': data }   
    return render(request, 'formulario5.html', context)  

def formularioParte6(request): 
    data =  CrudModel.objects.all()
    context = { 'employees': data }   
    return render(request, 'formulario6.html', context)   

def createView(request):
    form = CrudForm(request.POST or None)
    if form.is_valid():
        form.save(commit=False)
        form.save()
        messages.add_message(request, messages.SUCCESS, "Employee successfully added")
        return redirect('index')
    
    return redirect('index')      
    # return render(request,'index.html', { 'form': form })

def updateView(request, id):
    data= CrudModel.objects.get(id=id)
    form= CrudForm(request.POST or None, instance=data)
    if form.is_valid():
        form.save(commit=False)
        form.save()
        messages.add_message(request, messages.SUCCESS, "Employee successfully updated")
        return redirect('index')

    context= { 'employees': form }
    return render(request, 'index.html', context)   


def deleteView(request, id):
    data= CrudModel.objects.get(id=id)    
    data.delete()
    messages.add_message(request, messages.SUCCESS, "Employee successfully deleted")
    return redirect('index')

# Login
def cadastrar_usuario(request):
    if request.method == "POST":
        form_usuario = UserCreationForm(request.POST)
        if form_usuario.is_valid():
            form_usuario.save()
            messages.success(request, 'Conta criada com sucesso')
            return redirect('index')
    else:
        form_usuario = UserCreationForm()
    return render(request, 'cadastro.html', {'form_usuario': form_usuario})   

def logar_usuario(request):
    if request.method == "POST":
        username = request.POST["usuario"]
        password = request.POST["senha"]
        usuario = _Authenticator(request, username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('index')
        else:
            form_login = AuthenticationForm()
    else:
        form_login = AuthenticationForm()
    return render(request, 'login.html', {'form_login': form_login}) 

def index(request):
    return render(request, 'index.html')    