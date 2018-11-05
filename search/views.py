from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from index.models import Image
from index.models import Member
import json
from django.db.models import F

CATEGORY_CHOICES = [
	{'name': 'Abstract'},
	{'name': 'Aerial'},
	{'name': 'Animals'},
	{'name': 'Architecture'},
	{'name': 'Black and White'},
	{'name': 'Family'},
	{'name': 'Fashion'},
	{'name': 'Fine Art'},
	{'name': 'Food'},
	{'name': 'Journalism'},
	{'name': 'Landscape'},
	{'name': 'Macro'},
	{'name': 'Nature'},
	{'name': 'Night'},
	{'name': 'People'},
	{'name': 'Performing Arts'},
	{'name': 'Sport'},
	{'name': 'Still Life'},
	{'name': 'Street'},
	{'name': 'Travel'}
]

# Create your views here.
def index(request, browse_type='image'):
	categories=CATEGORY_CHOICES
	return render(request, 'browse.html', {'categories':categories, 'data':''})

def searchImage(request, search_type):
	keywords=json.loads(request.POST.get('keywords'))
	if(search_type=="tag"):
		images=list(Image.objects.filter(tags__name__in=keywords).distinct().values())
		return JsonResponse({'data':images})
	elif(search_type=="photographer"):
		photographer=Member.objects.filter(name__in=keywords)
		if(photographer):
			images=list(Image.objects.filter(photographer=photographer[0]).values())
		else:
			images=[]
	elif(search_type=="category"):
		images = list(Image.objects.filter(category=keywords[0]).values())
	return JsonResponse({'data':images})

def browse(request):
	categories=CATEGORY_CHOICES
	image_list=Image.objects.annotate(popularity=F('likes')+F('downloads')).order_by('-popularity')
	images=list(image_list.values())
	return render(request, 'browse.html', {'categories':categories, 'data':images})