from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {})

def add(request):
    from random import randint

    num_1 = randint(0,50)
    num_2 = randint(0,50)

    if request.method == "POST":
        answer = request.POST['answer']
        old_num_1 = request.POST['old_num_1']
        old_num_2 = request.POST['old_num_2']

        correct_answer = int(old_num_1) + int(old_num_2)
        if int(answer) == correct_answer:
            my_answer = "Correct! " + old_num_1 + " + " + old_num_2 + " = " + answer
            color = "success"
        else:
            my_answer = "Incorrect! " + old_num_1 + " + " + old_num_2 + " Doesn't equal " + answer + ", It is: " + str(correct_answer)
            color = "danger"

        return render(request, 'add.html', {'num_1': num_1, 'num_2': num_2, 'answer': answer, 'my_answer': my_answer, 'color': color,})
    
    return render(request, 'add.html', {
        'num_1':num_1,
        'num_2':num_2,
        })

def subtract(request):
    return render(request, 'subtract.html', {})

def multiply(request):
    return render(request, 'multiply.html', {})

def divide(request):
    return render(request, 'divide.html', {})