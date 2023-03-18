from django.db import models
from django.utils import timezone
import math
# Create your models here.
class User(models.Model):
    email = models.EmailField(unique=True,max_length=30,blank=False)
    password = models.CharField(max_length=15)
    role = models.CharField(max_length=15)
    is_active = models.BooleanField(default=False)
    is_varify = models.BooleanField(default=False)
    otp = models.IntegerField(default=456)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

class Chairman(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    contact_no = models.CharField(max_length=10)
    pic = models.FileField(upload_to="media/upload", default="media/chairman-default.png")
    

    def __str__(self):
        return self.firstname

class Societymember(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    contact_no = models.CharField(max_length=30)
    pic = models.FileField(upload_to="media/upload", default="media/chairman-default.png")

    def __str__(self):
        return self.firstname
    
class Notice(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE) 
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def count_view(self):
        ncount = NoticeViewDetails.objects.filter(notice_id = self.id).count()
        print("------------------>>>>",ncount)
        return ncount

    def whenpublished(self):
        now = timezone.now()

        diff = now - self.created_at

        if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
            seconds = diff.seconds

            if seconds == 1:
                return str(seconds) + " second ago"
            else:
                return str(seconds) + " seconds ago"
            
        if diff.days == 0 and diff.seconds >= 60 and diff.seconds < 3600:
            minutes = math.floor(diff.seconds/60)

            if minutes == 1:
                return str(minutes) + " minute ago"
            else:
                return str(minutes) + " minutes ago"
            
        if diff.days == 0 and diff.seconds >= 3600 and diff.seconds < 86400:
            hours = math.floor(diff.seconds/3600)

            if hours == 1:
                return str(hours) + " hour ago"
            else:
                return str(hours) + " hours ago"
            
        # 1 day to 30 days
        if diff.days >= 30 and diff.days < 365:
            months = math.floor(diff.days/30)

            if months == 1:
                return str(months) + " month ago"
            else:
                return str(months) + " months ago"
            
        if diff.days >= 365: 
            years = math.floor(diff.days/365)

            if years == 1:
                return str(years) + " year ago"
            else:
                return str(years) + " years ago"

class NoticeViewDetails(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    notice_id = models.ForeignKey(Notice,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Maintainance(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE) #chairman
    member_id = models.ForeignKey(Societymember,on_delete=models.CASCADE) # society member
    title = models.CharField(max_length=50)
    amount = models.CharField(max_length=50)
    duedate = models.DateField(max_length=50)
    status = models.CharField(max_length=50,default="PENDING")


class Event(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE) 
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    pic = models.FileField(upload_to="media/upload", default="media/chairman-default.png")

    def count_view(self):
        ecount = EventViewDetails.objects.filter(event_id = self.id).count()
        print("------------------>>>>",ecount)
        return ecount

    def whenpublishedevent(self):
        now = timezone.now()

        diff = now - self.created_at

        if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
            seconds = diff.seconds

            if seconds == 1:
                return str(seconds) + " second ago"
            else:
                return str(seconds) + " seconds ago"
            
        if diff.days == 0 and diff.seconds >= 60 and diff.seconds < 3600:
            minutes = math.floor(diff.seconds/60)

            if minutes == 1:
                return str(minutes) + " minute ago"
            else:
                return str(minutes) + " minutes ago"
            
        if diff.days == 0 and diff.seconds >= 3600 and diff.seconds < 86400:
            hours = math.floor(diff.seconds/3600)

            if hours == 1:
                return str(hours) + " hour ago"
            else:
                return str(hours) + " hours ago"
            
        # 1 day to 30 days
        if diff.days >= 30 and diff.days < 365:
            months = math.floor(diff.days/30)

            if months == 1:
                return str(months) + " month ago"
            else:
                return str(months) + " months ago"
            
        if diff.days >= 365: 
            years = math.floor(diff.days/365)

            if years == 1:
                return str(years) + " year ago"
            else:
                return str(years) + " years ago"

class EventViewDetails(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    notice_id = models.ForeignKey(Notice,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Complain(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE) 
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    pic = models.FileField(upload_to="media/upload")

    def count_view(self):
        ncount = ComplainViewDetails.objects.filter(complain_id = self.id).count()
        print("------------------>>>>",ncount)
        return ncount

    def whenpublishedcomplain(self):
        now = timezone.now()

        diff = now - self.created_at

        if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
            seconds = diff.seconds

            if seconds == 1:
                return str(seconds) + " second ago"
            else:
                return str(seconds) + " seconds ago"
            
        if diff.days == 0 and diff.seconds >= 60 and diff.seconds < 3600:
            minutes = math.floor(diff.seconds/60)

            if minutes == 1:
                return str(minutes) + " minute ago"
            else:
                return str(minutes) + " minutes ago"
            
        if diff.days == 0 and diff.seconds >= 3600 and diff.seconds < 86400:
            hours = math.floor(diff.seconds/3600)

            if hours == 1:
                return str(hours) + " hour ago"
            else:
                return str(hours) + " hours ago"
            
        # 1 day to 30 days
        if diff.days >= 30 and diff.days < 365:
            months = math.floor(diff.days/30)

            if months == 1:
                return str(months) + " month ago"
            else:
                return str(months) + " months ago"
            
        if diff.days >= 365: 
            years = math.floor(diff.days/365)

            if years == 1:
                return str(years) + " year ago"
            else:
                return str(years) + " years ago"

class ComplainViewDetails(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    notice_id = models.ForeignKey(Notice,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)



            





