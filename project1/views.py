from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from project1.models import ModelNikita


def index(request):
    return render(request, 'index.html')
def profile(request):

    return render(request, 'profile.html')
@csrf_exempt
def login(request):
    if request.method == 'GET':
        name = 'Egoor'
        return render(request, 'login.html', {'user': name})
    if request.method == 'POST':
        loginn = request.POST['login']
        password = request.POST['password']
        mail = request.POST['email']
        return redirect('/profile/')
        #return HttpResponse(f'Авторизация прошла успешно\nLogin: {loginn} Password: {password} Email: {mail}')
    return HttpResponse('Такой запрос непредусмотрен')

@csrf_exempt
def danger(request):
    if request.method == 'POST':
        nikita = ModelNikita()
        nikita.email = 'mail@testo.ua'
        nikita.password = '12456y'
        nikita.name = request.POST['name']
        nikita.save()
        print(f'{request.POST["name"]} запись сохранена!')
    return render(request, 'danger.html')