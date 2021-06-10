from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import CreateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import User
from .forms import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy

class register_new_user(CreateView):
    template_name = "register-user.html"
    form_class = UserCreationForm
    success_url = reverse_lazy('login')

@login_required(login_url='/login/')
def register_aluno(request):
    args = {'user': request.user}
    return render(request, 'register-aluno.html',args)

@login_required(login_url='/login/')
def accept_aluno(request):
    user = User.objects.filter(ativo=False)
    return render(request, 'accept.html',{'user':user})


def user_detail(request, id):
    user = User.objects.get(id=id)
    return render(request, 'accept2.html', {'user':user})

@login_required(login_url='/login/')
def delete_user(request, id):
    user1 = User.objects.get(id=id)
    user1.delete()
    return redirect('/')

@login_required(login_url='/login/')
def admin_accept_user(request, id):
    user1 = User.objects.get(id=id)
    user1.ativo = True
    user1.save()
    url = '/pet/all/'
    return redirect(url)


@login_required(login_url='/login/')
def list_login(request):
    return render(request, 'list.html')


@login_required(login_url='/login/')
def set_aluno(request):
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    email = request.POST.get('email')
    ano = request.POST.get('ano')
    matricula = request.POST.get('matricula')
    curso = request.POST.get('curso')
    user = request.user
    user.email = email
    user.ano = ano
    user.matricula = matricula
    user.curso = curso
    user.first_name = first_name
    user.last_name = last_name
    user.save()
    url = '/pet/all/'
    return redirect(url)

def logout_user(request):
    print(request.user)
    logout(request)
    return redirect('/login/')

def login_user(request):
    return render(request, 'login.html')

@csrf_protect
def submit_login(request):
    if request.POST:            #só aceitar a requisição se vier do tipo POST
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, "Usuário e senha Inválidos. Favor tente novamente.")
    return redirect('/login/')
