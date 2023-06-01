from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate

# Create your views here.


#Perfil de cada usuario
def profile(request):
    return render(request, 'profile.html')

#Función para el registro de usuarios
def signup(request):
    if request.method == 'POST':
        #Se realiza un request con toda la información necesaria para crear perfil
        primer_nombre = request.POST['primer_nombre']
        primer_apellido = request.POST['primer_apellido']
        username = request.POST['username']
        correo = request.POST['correo']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            #Validación en caso de que exista una cuenta con esas credenciales
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Una cuenta asociada a este correo ya existe')
                return redirect(signup)
            #Se crea el usuario
            else:
                user = User.objects.create_user(username=username, password=password, email=correo)
                user.set_password(password)
                user.is_staff = False
                user.save()
                print("success")
                return redirect('login')
    else:
        return render(request, 'signup.html')
    
    #Función para el Login
def login(request):
    if request.method == 'POST':
        #Se realiza una autenfificación de el usuario y su contraseña
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        #Validación en caso de que exista el usuario
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        #Validación en caso de que no exista el usuario o credenciales incorrectas
        else:
            messages.info(request, 'Usuario o contraseña incorrectas')
            return redirect('login')
    else:
        return render(request, 'login.html')

#Función para cerrar sesión
def logout(request):
    auth.logout(request)
    return redirect('index')
