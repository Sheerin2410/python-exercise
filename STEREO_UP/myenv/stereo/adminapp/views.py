from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect 
from .models import *
from random import*
from django.core.mail import send_mail
# Create your views here.

def home(request):
    if "email" in request.session:
        
            uid = User.objects.get(email = request.session['email'])
            if uid.role == "admin":
                aid = Admin.objects.get(user_id = uid)
                context = {
                            'uid' : uid,
                            'aid' : aid,
                        }
                return render(request,"adminapp/index.html",context)
            else:
                if uid.role == "member":
            
                    mid = Member.objects.get(user_id = uid)
                    context = {
                                'uid' : uid,
                                'mid' : mid,
                            }
                    return render(request,"adminapp/index.html",context)
    else:
            return redirect("login")
    
def login(request):
    if "email" in request.session:
        return redirect("home")
    else:
        if request.POST:
            pemail = request.POST['email']
            ppassword = request.POST['password']
            print("------------------email",pemail)

            try:
                uid = User.objects.get(email=pemail)
                if uid.password == ppassword:
                    if uid.role == "admin":
                        aid = Admin.objects.get(user_id=uid)
                        print("firstname: ",aid.firstname)
                        print(uid.role)
                        print(uid.password)
                        print("SIGN IN BUTTON CLICKED----------->" ,uid)
                        request.session['email'] = uid.email # session var store

                        return render(request,"adminapp/index.html")
                    else:
                        print("MEMBER") 
                        
                        if uid.role == "member":
                            mid = Member.objects.get(user_id=uid)
                            print("firstname: ",mid.firstname)
                            print(uid.role)
                            print(uid.password)
                            print("SIGN IN BUTTON CLICKED----------->" ,uid)
                            request.session['email'] = uid.email # session var store

                            return redirect("home")
                else:
                    context = {
                        'emsg' : "invalid password"
                    }
                    print("----->Something went wrong")   
                    return render(request,"adminapp/login.html",context)
            except:
                context = {
                        'emsg' : "invalid email adress"
                }
                print("----->Something went wrong")   
                return render(request,"adminapp/login.html",context)    
        else:
            print("========> LOGIN PAGE REFRESHED")
            return render(request,"adminapp/login.html")
        
def logout(request):
    if "email" in request.session:
        del request.session['email']
        return redirect("login")
    else:
        return redirect("login")
    
def admin_profile(request):
    if "email" in request.session:
        uid = User.objects.get(email=request.session['email'])
        aid = Admin.objects.get(user_id = uid)

        if request.POST:
            firstname = request.POST['firstname']
            lastname = request.POST['lastname']
 
            aid.firstname = firstname
            aid.lastname = lastname
            if "picture" in request.FILES:
                aid.pic = request.FILES['picture']
            aid.save()

            context = {
                        'uid' : uid,
                        'aid' : aid,
                    }
            return render(request,"adminapp/profile.html",context)
        else:
            context = {
                        'uid' : uid,
                        'aid' : aid,
                    }
            return render(request,"adminapp/profile.html",context)
           
    else:
        return redirect("login")
    
    
def admin_change_password(request):
    if "email" in request.session:
        uid = User.objects.get(email=request.session['email'])
        aid = Admin.objects.get(user_id = uid)

        if request.POST:
            currentpassword = request.POST['currentpassword']
            newpassword = request.POST['newpassword']
            if uid.password == currentpassword:
                uid.password == newpassword
                uid.save()
                return redirect("logout")
            else :
                pass
            context = {
                        'uid' : uid,
                        'aid' : aid,
                    }
            return render(request,"adminapp/profile.html",context)
    else:
        context = {
                    'uid' : uid,
                    'aid' : aid,
                }
        return render(request,"adminapp/profile.html",context)

def add_member(request):
    if "email" in request.session:
        uid = User.objects.get(email=request.session['email'])
        aid = Admin.objects.get(user_id = uid)
        if request.POST:
            firstname = request.POST['firstname']
            lastname = request.POST['lastname']
            email = request.POST['email']
            contactno = request.POST['contactno']
            l1 = ['bf76r6yh4f','gd67d4787','85uthf7fh','jhdhd883','nfuuf49ir','ted664g4h']
            password = email[4:7]+contactno[3:7]+choice(l1)

            uid = User.objects.create(email=email,password=password,role="member")
            mid = Member.objects.create(user_id = uid,firstname=firstname,lastname=lastname,contact_no=contactno)

            
            if mid:
                send_mail("STEREO UP Password","Your Password is: "+str(password),"shirinshaikh241020@gmail.com",[email])
                msg = "Successfully Member Created -- Plz check your email for password"
                context={
                    'msg' : msg,
                    'uid' : uid,
                    'aid' : aid,
                }
                return render(request,"adminapp/add-member.html",context)
        else:     

            context = {
                        'uid' : uid,
                        'aid' : aid,
                    }
             
            return render(request,"adminapp/add-member.html",context)
    else:
        return redirect("login")

    


    

