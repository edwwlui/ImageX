from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from index.models import Member,Image
from .forms import UploadImageForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from COMP3297_imageX.settings import GLOBAL_SETTINGS
# Create your views here.

@login_required
def index(request):
    if request.user.is_authenticated:
        member = Member.objects.get(user=request.user)
        if request.method == 'POST':
            form = UploadImageForm(request.POST,request.FILES)
            if form.is_valid():
                newImage = form.save(commit=False)
                newImage.photographer = member
                newImage.save()
                form.save_m2m()
                member.uploadQuota = member.uploadQuota + 1
                member.numberOfImage =member.numberOfImage + 1
                member.save()
                return render(request,'uploadSuccessfully.html')
            # print (form.errors)
        else:
            if member.uploadQuota > GLOBAL_SETTINGS['UPLOAD_QUOTA']:
                return render(request, 'uploadExceedUploadQuota.html')
            elif member.numberOfImage >= GLOBAL_SETTINGS['NO_OF_IMAGE']:
                return render(request, 'uploadExceedNoOfImage.html')
            form = UploadImageForm()
        return render(request, 'upload.html', {'form': form})