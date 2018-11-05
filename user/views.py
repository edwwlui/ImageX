from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .forms import UserCreationForm, UserProfileForm, AddProfileForm
from index.models import Member, User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
	return render(request, 'user.html')

def register(request):
	email=request.session['email']
	#logout(request)
	# return render(request, 'register.html', {'email':email})
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			newUser = form.save(commit=False)
			newUser.email = email
			newUser.save()
			return redirect('add_profile')
		# print (form.errors)
	else:
		form = UserCreationForm()
	return render(request, 'register.html', {'form': form})

def change_password(request):
	user=request.user
	if(request.method=='POST'):
		form=PasswordChangeForm(user, request.POST)
		if form.is_valid():
			user = form.save()
			update_session_auth_hash(request, user)  # Important!
			messages.success(request, 'Your password was successfully updated!')
			return redirect('change_password')
	else:
		form=PasswordChangeForm(user)
	return render(request, 'changePassword.html', {'form':form})

@login_required
def edit_profile(request):
	if request.user.is_authenticated:
		if(request.method=='POST'):
			form=UserProfileForm(request.POST or None, request.FILES or None)
			if form.is_valid():
				newProfile = form.save(commit=False)
				member = Member.objects.get(user=request.user)
				if newProfile.name is not None:
					member.name = newProfile.name
				if newProfile.contact is not None:
					member.contact = newProfile.contact
				if newProfile.description is not None:
					member.description = newProfile.description
				if newProfile.avatarImage is not None:
					member.avatarImage = newProfile.avatarImage
				if newProfile.location is not None:
					member.location = newProfile.location
				member.save()
				return render(request,'editProfileSuccessfully.html')
		else:
			form=UserProfileForm()
		return render(request, 'editProfile.html', {'form':form})

def add_profile(request):
	if request.method == 'POST':
		form = AddProfileForm(request.POST)
		if form.is_valid():
			newProfile = form.save(commit=False)
			user = User.objects.get(email=request.session['email'])
			Member.objects.create(user=user, name=newProfile.name, description=newProfile.description)
			return render(request,'registerSuccessfully.html')
	else:
		form = AddProfileForm()
	return render(request, 'addProfile.html', {'form': form})
