from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Saikhah Ummu Anja Amalia',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)
