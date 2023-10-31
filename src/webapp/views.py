
from django.contrib.auth import authenticate, login
from django.contrib import messages, admin
from .decorator import unauthenticated_user
from django.shortcuts import redirect, render
from django.http import HttpResponse, request
from webapp.models import User, Comunicado
from webapp.forms import RegistrationForm
from django.template import RequestContext


# Create your views here.

def home(request):
    Comunicados = Comunicado.objects.all().order_by('-fecha_ultima_modificacion')
    Usuarios = User.objects.all().order_by('username')
    DTS = {
        'Comunicados': Comunicados,
        'Usuarios': Usuarios,}
    #NO LOGRO QUE SE VEAN LOS COMUNICADOS AYUDA NO DUERMO HACE 2DIAS
    return render(request, 'webapp/body.html',DTS) 


def register_view(request, *args, **kwargs):
    return render(request, 'webapp/register.html', {})


@unauthenticated_user
def loginPage(request):
    
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect("{% url 'home' %}")
        else:
            messages.info(request, 'Usuario o contraseña incorrecta')
                
    context = {}
    return render(request, 'webapp/login.html', context)

def register_view(request, *args, **kwargs):
    user = request.user
    if user.is_authenticated:
        return HttpResponse("Ya se encuentra registrado " + str(user.email))
    context = {}

    if request.POST:
        form = RegistrationForm(request.POST)
        
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            destination = kwargs.get("next")
            if destination:
                return redirect(destination)
            return redirect(home)
        else:
            
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'webapp/register.html', context)

