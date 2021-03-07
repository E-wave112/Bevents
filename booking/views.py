from django.shortcuts import render
from .forms import AuthUserCreationForm
from rest_framework import generics ##i norder to add some serializers

# Create your views here.

def register(request):
    if request.method == 'POST':
        user_form = AuthUserCreationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request,
            'account/register_done.html',
            {'new_user': new_user})
    else:
        user_form = AuthUserCreationForm()
    return render(request,'account/register.html', {'user_form': user_form})

# ##createe a class based login api view in rest framework
# class LoginAPIView(generics.ListCreateAPIView):
    
