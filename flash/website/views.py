from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {})

def add(request):
    if request.method == "POST":
        answer = request.POST['answer']
        return render(request, 'add.html', {'answer':answer})
    return render(request, 'add.html', {})

def subtract(request):
    return render(request, 'subtract.html', {})

def multiply(request):
    return render(request, 'multiply.html', {})

def divide(request):
    return render(request, 'divide.html', {})