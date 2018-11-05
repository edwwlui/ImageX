from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from taggit.managers import TaggableManager

CATEGORY_CHOICES = (
    ('Abstract', 'Abstract'),
    ('Aerial', 'Aerial'),
    ('Animals', 'Animals'),
	('Architecture', 'Architecture'),
	('Black and White', 'Black and White'),
	('Family', 'Family'),
	('Fashion', 'Fashion'),
	('Fine Art', 'Fine Art'),
	('Food', 'Food'),
	('Journalism', 'Journalism'),
	('Landscape', 'Landscape'),
	('Macro', 'Macro'),
	('Nature', 'Nature'),
	('Night', 'Night'),
	('People', 'People'),
	('Performing Arts', 'Performing Arts'),
	('Sport', 'Sport'),
	('Still Life', 'Still Life'),
	('Street', 'Street'),
	('Travel', 'Travel')
)

# Create your models here.
class Member(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=20, blank=True, null=True)
	contact = models.CharField(max_length=20, blank=True, null=True)
	description = models.CharField(max_length=255, blank=True, null=True)
	avatarImage = models.ImageField(upload_to='avatar/', validators=[FileExtensionValidator(allowed_extensions=['jpg'])], blank=True, null=True)
	location = models.CharField(max_length=50, blank=True, null=True)
	uploadQuota = models.IntegerField(default=0)
	numberOfImage = models.IntegerField(default=0)
	def __str__(self):
		return self.user.username

class Curator(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	def __str__(self):
		return self.user.username

class Image(models.Model):
	title = models.CharField(max_length=20, blank=True)
	description = models.CharField(max_length=255, blank=True)
	tags = TaggableManager(blank=True)
	category = models.CharField(blank=True, max_length=20, choices=CATEGORY_CHOICES, null=True)
	file = models.ImageField(upload_to='images/', validators=[FileExtensionValidator(allowed_extensions=['jpg'])])
	
	time = models.DateTimeField(auto_now_add=True)
	
	likes = models.IntegerField(default=0)
	downloads = models.IntegerField(default=0)
	photographer = models.ForeignKey(Member, related_name="member_photographer",null=True, on_delete=models.CASCADE)
	LikedMember=models.ManyToManyField(Member, related_name="member_liked", blank=True)

	def __str__(self):
		return self.title

class Gallery(models.Model):
	name = models.CharField(max_length=20)
	images = models.ManyToManyField(Image, blank=True)
	category = models.CharField(blank=True, max_length=20, choices=CATEGORY_CHOICES, null=True)
	tags = TaggableManager()
	def __str__(self):
		return self.name

class ResetPasswordRequest(models.Model):
	email = models.EmailField(blank=True)
	sent = models.BooleanField(default=False)
	def sendEmail(self):
		self.sent=True
		self.save()
