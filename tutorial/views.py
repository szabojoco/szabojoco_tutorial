from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.contrib import messages
from tutorial.forms import UserForm
from .models import Tutorial, UserTutorialPurchased


# View for listing all tutorials
def tutorial_view(request):
    my_objects = Tutorial.objects.all()
    return render(request, 'tutorial/tutorial.html', {'tutorials': my_objects})


# View for displaying details of a tutorial
def tutorial_detail(request, tutorial_id):
    tutorial = Tutorial.objects.get(id=tutorial_id)
    return render(request, 'tutorial/tutorial_detail.html', {'tutorial': tutorial})


# View for purchasing a tutorial
@login_required
def tutorial_buy(request, tutorial_id):
    tutorial = get_object_or_404(Tutorial, pk=tutorial_id)

    if UserTutorialPurchased.objects.filter(user=request.user, tutorial=tutorial).exists():
        messages.error(request, "You have already purchased this tutorial.")
        return redirect('purchased_tutorial', tutorial_id=tutorial_id)

    return render(request, 'tutorial/tutorial_buy.html', {'tutorial': tutorial})


# View for displaying the content of a purchased tutorial
@login_required
def tutorial_content(request, tutorial_id):
    tutorial = get_object_or_404(Tutorial, id=tutorial_id)

    if UserTutorialPurchased.objects.filter(user=request.user, tutorial=tutorial).exists():
        return render(request, 'tutorial/tutorial_content.html', {'tutorial': tutorial})
    else:
        return redirect('tutorial_detail', tutorial_id=tutorial_id)


# View for listing user's purchased tutorials
@login_required
def my_tutorials(request):
    user = request.user
    purchased_tutorials = UserTutorialPurchased.objects.filter(user=user)

    return render(request, 'tutorial/my_tutorials.html', {
        'purchased_tutorials': purchased_tutorials,
    })


# View for processing tutorial payment
@login_required
def process_payment(request, tutorial_id):
    if request.method == 'POST':
        tutorial = Tutorial.objects.get(id=tutorial_id)
        UserTutorialPurchased.objects.create(user=request.user, tutorial=tutorial)
        return redirect('purchased_tutorial', tutorial_id=tutorial_id)
    else:
        return redirect('tutorial_detail', tutorial_id=tutorial_id)


# View for displaying purchased tutorial details
@login_required
def purchased_tutorial(request, tutorial_id):
    tutorial = get_object_or_404(Tutorial, id=tutorial_id)
    return render(request, 'tutorial/purchased_tutorial.html', {'tutorial': tutorial})


# View for successful purchase message
@login_required
def purchased_successful(request):
    return render(request, 'tutorial/purchased_successful.html')


# View for displaying the content of a purchased tutorial
@login_required
def content_view(request, tutorial_id):
    tutorial = get_object_or_404(Tutorial, id=tutorial_id)

    if UserTutorialPurchased.objects.filter(user=request.user, tutorial=tutorial).exists():
        return render(request, 'tutorial/content.html', {'tutorial': tutorial})
    else:
        return redirect('tutorial_detail', tutorial_id=tutorial_id)


# View for user sign up
def sign_up(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserForm()

    return render(request, 'registration/sign_up.html', {'form': form})


# View for user login
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()

    return render(request, 'registration/login.html', {'form': form})


# View for the home page (if needed)
class HomeTemplateView(TemplateView):
    template_name = "home/home.html"
