from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from login_app import forms

#
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

# login_required decorator provides functionality to preset views when logged in
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return HttpResponse("Hello World")

def app_index(request):
    return render(request, 'index.html', context = {'titile' : 'Index'})

def vw_contact_me(request):
    
    if request.method == 'POST':
        contactForm = forms.contact_me_form(request.POST)
        print(contactForm)
        print([x for x in request.POST])
        if contactForm.is_valid():
            contactForm.save()
            return render(request, 'index.html', context = {'titile' : 'Sinex',
                                                            'message' : 'Thanks! We will contact you soon.',
                                                            })
    
    return render(request, 'login_app/contact_me.html', context = {
                                                    'title' : 'Contact Me',
                                                    'form' : forms.contact_me_form,
                                                })

def userRegistration(request):
    
    registered = False
    
    if request.method == 'POST':
        form_user_data = forms.UserProfileForm(data=request.POST)
        form_extension_data = forms.UserProfileExtention(data=request.POST)
        
        if form_user_data.is_valid and form_extension_data.is_valid:
            
            # Saving directly to database
            user = form_user_data.save()
            
            # Hasing the password and saving again using 'set_password' method
            # :: Parent table is filled
            user.set_password(user.password)
            user.save()
            
            # profile extention data is not directly saved to DB bcz this will 
            # add extra record and one to one relationship will not be satisfied
            profile = form_extension_data.save(commit=False)
            
            # named dictionary's attribute user is made equal to 'user' to 
            # satisfy one to one relationship with this model.
            # NOTICE: Here we are passing complete model object to user feild. Bcz 
            # model is mapped not any one feild
            # :: Child table is linked to parent model (kind of FK)
            profile.user = user
            
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
                
            # :: Child table is loaded
            profile.save()
            
            registered = True
            
            return render(request, 'index.html', context = {'titile' : 'Success!',
                                                            'message' : 'Registered Successfully',
                                                            })
            
        else:
            HttpResponse("User form is Invalid!")
            print(form_user_data.errors, form_extension_data.errors)
        
    return render(request, 'login_app/registration.html', context = {
                'title' : 'Registration!',
                'form_user' : forms.UserProfileForm,
                'form_extention' : forms.UserProfileExtention,
            })


@login_required
def vw_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def special(request):
    return HttpResponse("You are alredy logged in")


def vw_login(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(request.body)
        print([x for x in request.POST])
        # Using Django built-in authentication function
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
        
            else:
                return HttpResponse("Account not Active")
    
        else:
            print(f"Username: {username} tried to login with password: {password}")
            return render(request, 'index.html', context = {'titile' : 'Success!',
                                                            'message' : 'You are not registered!',
                                                            })
    
    return render(request, 'login_app/login.html', context={'title':'Login'})
