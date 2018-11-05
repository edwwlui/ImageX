from index.models import Member
from index.models import Curator
from django.utils.deprecation import MiddlewareMixin

class checkUserTypeMiddleware(MiddlewareMixin):
	def process_request(self, request):
		if request.user.is_authenticated:
			if(Member.objects.filter(user_id=request.user.id).exists()):
				request.session['userType']='member'
			elif (Curator.objects.filter(user_id=request.user.id).exists()):
				request.session['userType']='curator'
			else:
				request.session['userType']='admin'
		else:
			request.session['userType']='user'
		return None
