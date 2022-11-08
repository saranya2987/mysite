from django.shortcuts import redirect, render
from users.forms import NewUserForm
from django.contrib.auth.decorators import login_required
from .models import Profile
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

def profile(request):

    pro = Profile.objects.get(user=request.user)
    context = {'profile':pro}
    return render(request, 'users/profile.html',context=context)

def createprofile(request):
    if request.method =="POST":
        contact_number = request.POST.get('contact_number')
        image =request.FILES['upload']
        pro = Profile()
        pro.contact_number =contact_number
        pro.image=image
        pro.user=request.user
        pro.save()
        return redirect('users/profile.html')

    return render(request, 'users/createprofile.html')
