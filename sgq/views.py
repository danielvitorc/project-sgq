from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import Group



# ===== Tela de Login ===== 
def login_usuario(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
                        # Redirecionar de acordo com o grupo do usuário
            if user.groups.filter(name='COORDENADORES').exists():
                return redirect('home-coordenador')
            elif user.groups.filter(name='SUPERVISORES').exists():
                return redirect('home-sup')
            elif user.groups.filter(name='ADMINISTRADORES').exists():
                return redirect('home-adm')
            else:
                return redirect('home')  
        else:
            messages.error(request, 'Usuário ou senha inválidos.')
    return render(request, 'sgq/login.html')

# ===== Renderizar a tela Home para cada acesso se o login for bem sucedido =====
@login_required
def coordenadores(request):
    return render(request, 'sgq/home-coordenador.html')

@login_required
def supervisores(request):
    return render(request, 'sgq/home-sup.html')

@login_required
def administradores(request):
    return render(request, 'sgq/home-adm.html')

@login_required
def home(request):
    return render(request, 'sgq/home.html')

# ==== Função para deslogar do sistema =====
def logout_usuario(request):
    logout(request)
    return redirect('login')