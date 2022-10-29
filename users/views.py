from django.shortcuts import render
from users.forms import NewUserForm

# Create your views here.
def register(request):
    form = NewUserForm(request.POST)
    if request.method =='POST':
        print(form.is_valid())

    context ={
        'form': form,
    }

    return render(request, 'users/register.html',context=context)
