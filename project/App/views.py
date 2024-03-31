from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from .models import studentDetails

def home(request):
    return render(request, "student/index.html")


def register(request):
    if request.method == "POST":
        name = request.POST.get('name')
        University = request.POST.get('University')
        branch = request.POST.get('branch')
        session = request.POST.get('session')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('pass1')
        data = studentDetails(name=name, University=University, branch=branch, session=session, email=email, phone=phone, Password=Password)
        print(data)  # Check if data is being constructed properly
        try:
            data.save()
            print("Data saved successfully")  # Check if data is saved successfully
        except Exception as e:
            print("Error saving data:", e)  # Print any errors that occur during data saving
        return redirect('login')
    return render(request, "../template/student/registration.html")



def user_login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            auth_login(request, user)
            # Redirect to a success page.
            return redirect('dashboard')  # Assuming 'dashboard' is the name of your dashboard URL
        else:
            # Return an 'invalid login' error message.
            return render(request, "../template/student/login.html", {'error_message': 'Invalid login'})
    return render(request, "../template/student/login.html")
