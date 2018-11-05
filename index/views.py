from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Image, Member
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.files import File
from django.db.models import F

from .forms import PasswordResetForm
from django.contrib import messages

import os
# Create your views here.
def index(request):
	#image=Image.objects.get(pk=1)
	#context={'image':image}
	#return render(request, 'index.html', context)
	image_list=Image.objects.annotate(popularity=F('likes')+F('downloads')).order_by('-popularity')[:5]
	images=list(image_list.values())
	return render(request, 'index.html', {'images':images})
	# else:
	# 	url0=settings.MEDIA_URL+str(image_list[0].file)
	# 	url1=settings.MEDIA_URL+str(image_list[1].file)
	# 	url2=settings.MEDIA_URL+str(image_list[2].file)
	# 	image0=str(image_list[0].id)
	# 	image1=str(image_list[1].id)
	# 	image2=str(image_list[2].id)
	# 	context={'url0':url0, 'url1':url1, 'url2':url2, 'image0':image0, 'image1':image1,'image2':image2}
	# 	return render(request, 'index.html',context)

@login_required
def delete(request, image_id):
	image=Image.objects.filter(pk=image_id)[0]
	member = Member.objects.filter(user=request.user)[0]
	try:
		#only delete one's own
		if(image.photographer!=member):
		 	return render(request, 'index.html', {'error_message': "NOT ALLOWED"})
		member.numberOfImage-=1
		member.save()
		image.delete()
	#doesnotexist
	except (KeyError, Image.DoesNotExist):
		return render(request, 'index.html', {'error_message': "NOT EXIST"})
	else:
		return HttpResponseRedirect("/")

@login_required
def like(request, image_id):
	image=Image.objects.filter(pk=image_id)[0]
	member = Member.objects.filter(user=request.user)[0]
	try:
		#cannot like one's own
		if(image.photographer==member):
		 	return HttpResponseRedirect("/image/"+str(image.id))
		#if member has liked
		for likedmember in image.LikedMember.all():
			if member==likedmember:
				return HttpResponseRedirect("/image/"+str(image.id))
		image.likes+=1
		#need to save b4 association
		image.save()
		image.LikedMember.add(member)
		return HttpResponseRedirect("/image/"+str(image.id))
		
	#doesnotexist
	except (KeyError, Image.DoesNotExist):
		return render(request, 'index.html', {'error_message': "Not exist"})
	else:
		return HttpResponseRedirect("/")

def download(request,image_id):
	try:
		image_download=Image.objects.get(pk=image_id)
		image_download.downloads+=1
		image_download.save()
		file_path = os.path.join(settings.MEDIA_ROOT, str(image_download.file))
		if os.path.exists(file_path):
			with open(file_path, 'rb') as fh:
				response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
				response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
				return response
			raise Http404
		return HttpResponseRedirect("/")
	except (KeyError, Image.DoesNotExist):
		return render(request, 'index.html', {'error_message': "Not exist"})
	else:
		return HttpResponseRedirect("/")

def viewImage(request, image_id):
    image = Image.objects.get(pk=image_id)
    member_viewing_own=False
    if request.user.is_anonymous==False:
	    member = Member.objects.get(user=request.user)
	    if image.photographer==member:
	    	member_viewing_own=True
	    else:
	    	member_viewing_own=False

    owner = "none"

    if request.user.is_authenticated:
        if image.photographer.user.username == request.user.username:
            owner = "inline"



    output = {'image': image,
            'tags' : list(image.tags.names()),
			'owner' : owner,
			'member_viewing_own':member_viewing_own}

    return render(request, 'details.html', output)

def viewProfile(request, user_id):
    user = User.objects.get(pk=user_id)
    member = Member.objects.get(user=user)
    images=list(Image.objects.filter(photographer=member).values())
    owner = "none"

    if request.user.is_authenticated:
        if user == request.user:
            owner = "inline-block"

    output = {'member': member,
			'owner': owner,
			'data':images}

    return render(request, 'viewProfile.html', output)

# def viewImageAll(request):
# 	all_images = Image.objects.all()
# 	list = []
# 	for image in all_images:
# 		html = '<p> Image #{id} {title} at {time}</b></p>'
# 		list.append(html.format(id=image.id, title=image.title, time=image.time))
# 	output = '<hr>'.join(list)
# 	return HttpResponse(output)

# def viewMemberAll(request):
# 	all_members = Member.objects.all()
# 	list = []
# 	for member in all_members:
# 		html = '<p> Member #{id} upload quota = {uploadQuota}, no of Image = {numberOfImage}</b></p>'
# 		list.append(html.format(id=member.id, uploadQuota=member.uploadQuota, numberOfImage=member.numberOfImage))
# 	output = '<hr>'.join(list)
# 	return HttpResponse(output)

def password_reset(request):
	if request.method == 'POST':
		form=PasswordResetForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Your request has been sent to the admin')
			return redirect('password_reset')
	else:
		form = PasswordResetForm()
	return render(request, 'registration/password_reset_form.html', {'form': form})


