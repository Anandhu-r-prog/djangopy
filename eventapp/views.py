
from .forms import LoginForm, SignupForm, BookingForm, UserSuggestionForm,BeachWeddingForm
from . models import Event, LoginRecord,SignupData
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib import messages
from .forms import UserMessageForm
from django.contrib.auth.hashers import make_password


def Homeindex(request):
    form = UserSuggestionForm()
    return render(request, 'homeindex.html', {'form': form})

def Booking(request):
    return render(request,'Booking.html')
def about(request):
    return render(request,'about.html')


     
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # Save the login attempt to database
            LoginRecord.objects.create(email=form.cleaned_data['email'])
            messages.success(request, "Login recorded!")
            return redirect('login')  # Or any dashboard
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})
    

def form_success(request):
    return render(request, 'form_success.html')



def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            
            full_name = form.cleaned_data['full_name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            password = form.cleaned_data['password']

            user = SignupData(
                full_name=full_name,
                email=email,
                phone=phone,
            )
            user.password = make_password(password)  # Important to hash password!
            user.save()

            return redirect('login') 
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})




 

def weddings(request):
    return render (request,'weddings.html')


def service(request):
    serve={
        'eve':Event.objects.all()
        
    }

    return render(request,'service.html',serve)
def venues(request):
    return render(request,'venues.html')
def Reserve(request):
    return render(request,'reserve.html')
def contact(request):
    return render(request,'contact.html')
def musical(request):
    return render(request,'musical.html')
def parties(request):
    image_range = range(1, 9)  
    return render(request, 'parties.html', {'image_range': image_range})

def corporate(request):
    return render(request,'corporate.html')

def myfile(request):
    return render(request,'myfile.html')
def allweddings(request):
    return render(request, 'allweddings.html')

def create(request):
    if request.method == 'POST':
        form = UserMessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('form_success')
    else:
        form = UserMessageForm()
    return render(request, 'create.html', {'form': form})

def service_page(request):
    return render(request, 'Servicemain.html')



def book_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'success.html')  # You can customize this page
    else:
        form = BookingForm(initial={'event': event})
    return render(request, 'book_event.html', {'form': form, 'event': event})

# def suggestion_view(request):
#     if request.method == 'POST':
#         form = UserSuggestionForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('thank_you')  # You can create a thank you page or show message
#     else:
#         form = UserSuggestionForm()
#     return render(request, 'suggestion.html', {'form': form})

def suggestion_view(request):
    if request.method == 'POST':
        form = UserSuggestionForm(request.POST)
        if form.is_valid():
            suggestion = form.save()
            print("Suggestion saved:", suggestion)  # Debug line
            return redirect('Homeindex')  # Change to a working redirect
        # else:
        #     print("Form errors:", form.errors)  # Debug errors
        else:
            print(form.errors) 
    else:
        form = UserSuggestionForm()
    return render(request, 'contact.html', {'form': form})

def book_weddings(request):
    if request.method == 'POST':
        form = BeachWeddingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booking_success')  # Redirect to a thank-you or confirmation page
    else:
        form = BeachWeddingForm()
    return render(request, 'weddings.html', {'form': form})