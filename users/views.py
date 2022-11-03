from django.shortcuts import redirect, render
from users.forms import NewUserForm

# Create your views here.
def register(request):
    print('ooooooooooooooooooooooooooooooooooooooooooooooooooo')
    form = NewUserForm(request.POST)    
    if request.method =='POST':
        # print(form.is_valid)
        print(f'form valid: {form.is_valid()}')

        if form.is_valid():
            form.save()
        return redirect('/myapp/products')

    context ={
        'form': form,
    }

    return render(request, 'users/register.html',context=context)
