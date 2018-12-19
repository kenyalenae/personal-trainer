from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from .forms import ContactForm


# function for home page
def home(request):
    return render(request, 'trainer/home.html')


# function for account home page which is for when the user is logged in
def accountHome(request):
    return render(request, 'trainer/accountHome.html')


# function for about page
def about(request):
    return render(request, 'trainer/about.html', {'title': 'About'})


# function for workout program page
def workoutProgram(request):
    return render(request, 'trainer/workout_program.html', {'title': 'Workout Program'})


# function for meal plan page
def mealPlan(request):
    return render(request, 'trainer/meal_plan.html', {'title': 'Meal Plan'})


# function for contact form
def emailView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, 'trainer/contact.html', {'form': form})


# function for the success message that displays after user sends message using contact form
def successView(request):
    return render(request, 'trainer/contact_success.html')
