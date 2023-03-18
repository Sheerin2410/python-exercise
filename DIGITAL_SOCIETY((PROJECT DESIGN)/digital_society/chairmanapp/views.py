from random import choice
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect 
from .models import *
from random import*
from django.core.mail import send_mail

# Create your views here.
"""
get() : returns object

models.objects.get(fieldname = htmlname) ->for fetch data from database (model)

uid = models.objects.get()
uid.fieldname = newvalue
uid.save()   :   for update data

# to store data in model (similar like inser query)
uid = models.objects.create(fieldname=pythonname,fieldname=pythonname)

# fetch all data from model (without any condition)

var = models.objects.all()

e.g, Notice.objects.all()

# fetch all data from model with condition

--- > filter() : returns queryset

var = models.objects.filter(fieldname=value)


"""
# def login_backend(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         uid = authenticate(username=username, password=password)
#         if uid is not None:
#             login(request, uid)
#             request.session.set_expiry(300)
#             return HttpResponseRedirect('/overview/')
#         else:
#             return HttpResponseRedirect('login')
#     else:
#         return render_to_response('login.html', context_instance=RequestContext(request))
def home(request):
    if "email" in request.session:
        
            uid = User.objects.get(email = request.session['email'])
            if uid.role == "chairman":
                cid = Chairman.objects.get(user_id = uid)
                context = {
                            'uid' : uid,
                            'cid' : cid,
                        }
                return render(request,"chairmanapp/index.html",context)
            else:
                if uid.role == "societymember":
            
                    sid = Societymember.objects.get(user_id = uid)
                    context = {
                                'uid' : uid,
                                'sid' : sid,
                            }
                    return render(request,"societymemberapp/index.html",context)
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
                    if uid.role == "chairman":
                        cid = Chairman.objects.get(user_id=uid)
                        print("firstname: ",cid.firstname)
                        print(uid.role)
                        print(uid.password)
                        print("SIGN IN BUTTON CLICKED----------->" ,uid)
                        request.session['email'] = uid.email # session var store

                        return redirect("home")
                    else:
                        print("SOCIETY MEMBER") 
                        
                        if uid.role == "societymember":
                            sid = Societymember.objects.get(user_id=uid)
                            print("firstname: ",sid.firstname)
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
                    return render(request,"chairmanapp/login.html",context)
            except:
                context = {
                        'emsg' : "invalid email adress"
                }
                print("----->Something went wrong")   
                return render(request,"chairmanapp/login.html",context)    
        else:
            print("========> LOGIN PAGE REFRESHED")
            return render(request,"chairmanapp/login.html")
def logout(request):
    if "email" in request.session:
        del request.session['email']
        return redirect("login")
    else:
        return redirect("login")
    
def chairman_profile(request):
    if "email" in request.session:
        uid = User.objects.get(email=request.session['email'])
        cid = Chairman.objects.get(user_id = uid)

        if request.POST:
            firstname = request.POST['firstname']
            lastname = request.POST['lastname']
 
            cid.firstname = firstname
            cid.lastname = lastname
            if "picture" in request.FILES:
                cid.pic = request.FILES['picture']
            cid.save()

            context = {
                        'uid' : uid,
                        'cid' : cid,
                    }
            return render(request,"chairmanapp/profile.html",context)
        else:
            context = {
                        'uid' : uid,
                        'cid' : cid,
                    }
            return render(request,"chairmanapp/profile.html",context)
           
    else:
        return redirect("login")
    
def chairman_change_password(request):
    if "email" in request.session:
        uid = User.objects.get(email=request.session['email'])
        cid = Chairman.objects.get(user_id = uid)

        if request.POST:

            currentpassword = request.POST['currentpassword']
            print("==========currentpassword",currentpassword)
            newpassword = request.POST['newpassword']
            print("==========newpassword",newpassword)
            if uid.password == currentpassword:
                uid.password =newpassword
                uid.save()
                return redirect("logout")
            else :
                pass
                context = {
                        'uid' : uid,
                        'cid' : cid,
                    }
        return render(request,"chairmanapp/profile.html",context)
    else:
        context = {
                    'uid' : uid,
                    'cid' : cid,
                }
        return render(request,"chairmanapp/profile.html",context)
    
def add_member(request):
    if "email" in request.session:
        uid = User.objects.get(email=request.session['email'])
        cid = Chairman.objects.get(user_id = uid)
        if request.POST:
            firstname = request.POST['firstname']
            lastname = request.POST['lastname']
            email = request.POST['email']
            contactno = request.POST['contactno']
            l1 = ['bf76r6yh4f','gd67d4787','85uthf7fh','jhdhd883','nfuuf49ir','ted664g4h']
            password = email[4:7]+contactno[3:7]+choice(l1)

            uid = User.objects.create(email=email,password=password,role="societymember")
            sid = Societymember.objects.create(user_id = uid,firstname=firstname,lastname=lastname,contact_no=contactno)

            
            if sid:
                send_mail("Digital Society Password","Your Password is: "+str(password),"shirinshaikh241020@gmail.com",[email])
                msg = "Successfully Societymember Created -- Plz check your email for password"
                context={
                    'msg' : msg,
                    'uid' : uid,
                    'cid' : cid,
                }
                return render(request,"chairmanapp/add-member.html",context)
        else:     

            context = {
                        'uid' : uid,
                        'cid' : cid,
                    }
             
            return render(request,"chairmanapp/add-member.html",context)
    else:
        return redirect("login")
    
def add_notice(request):
    if "email" in request.session:
        uid = User.objects.get(email=request.session['email'])
        cid = Chairman.objects.get(user_id = uid)
        if request.POST:
            nid = Notice.objects.create(
                 user_id = uid,
                 title = request.POST['title'],
                 description = request.POST['description']

            )
            nall = Notice.objects.all()
            context = {
                    'uid' : uid,
                    'cid' : cid,
                    'nall' : nall,
                }
            return render(request,"chairmanapp/notice-list.html",context)
        else:
            context = {
                        'uid' : uid,
                        'cid' : cid,
                    }
            return render(request,"chairmanapp/add-notice.html",context)
    else:
        return redirect("login")
    
def view_notice(request):
    if "email" in request.session:
        uid = User.objects.get(email=request.session['email'])
        cid = Chairman.objects.get(user_id = uid)
        nall = Notice.objects.all()
        context = {
                    'uid' : uid,
                    'cid' : cid,
                    'nall' : nall,
                }
        return render(request,"chairmanapp/notice-list.html",context)
    else:
        return redirect("login")
    
def view_notice_details(request,pk):
    if "email" in request.session:
        print("----------------------->PK",pk)
        uid = User.objects.get(email=request.session['email'])
        cid = Chairman.objects.get(user_id = uid)
        notice = Notice.objects.filter(id = pk)
        context = {
                    'uid' : uid,
                    'cid' : cid,
                    'notice' : notice,
                }
        return render(request,"chairmanapp/notice-details.html",context)
    else:
        return redirect("login")    
    

def all_societymembers(request):
    if "email" in request.session:
        uid = User.objects.get(email=request.session['email'])
        cid = Chairman.objects.get(user_id = uid)

        sall = Societymember.objects.all()
        context = {
                    'uid' : uid,
                    'cid' : cid,
                    'sall' : sall,
                }
        return render(request,"chairmanapp/all-societymembers.html",context) 

def societyspecification_profile(request,pk):
    if "email" in request.session:
        uid = User.objects.get(email=request.session['email'])
        cid = Chairman.objects.get(user_id = uid)
        sid = Societymember.objects.get(id = pk)
        context = {
                    'uid' : uid,
                    'cid' : cid,
                    'sid' : sid,
                }
        return render(request,"chairmanapp/specific-profile.html",context) 
    
def forgot_password(request):
    if request.POST:
        email = request.POST['email']
        otp = randint(1111,9999)

        try:
            uid = User.objects.get(email = email)
            uid.otp = otp
            uid.save()
            send_mail("Forgot Password","Your OTP is : "+str(otp),"shirinshaikh241020@gmail.com",[email])
            context={
                'email' : email
            }
            return render(request,"chairmanapp/change-password.html",context)  
        except Exception as e:
            print("-------------------------->>E",e)
            context={
                "emsg" : "Invalid Email Address"
            }
            return render(request,"chairmanapp/forgot-password.html",context) 

    return render(request,"chairmanapp/forgot-password.html") 

def change_password_value(request):
    if request.POST:
        email = request.POST['email']
        print("================>EMAIL : ",email)
        newpassword = request.POST['newpassword']
        print("================>",newpassword)
        
        confirmpassword = request.POST['confirmpassword']
        print("================>confirm PASSWORD : ",confirmpassword)
       
        otp = request.POST['otp']

        uid = User.objects.get(email = email)
        if str(uid.otp) == otp:
            if  uid.password == confirmpassword:
                uid.password = newpassword
                uid.save()
                context ={
                "email" : email,    
                "smsg" : "PASSWORD SUCCESSFULLY CHANGED"
                 }
                return render(request,"chairmanapp/login.html",context)
            else:
                emsg = "INVALID PASSWORD"
                context ={
                "email" : email,   
                'emsg' : emsg
                 }
            return render(request,"chairmanapp/change-password.html",context)
            
        else:
            emsg= "INVALID OTP"
            context ={
                "email" : email,
                'emsg' : emsg
            }
            return render(request,"chairmanapp/change-password.html",context)
        
def add_maintainance(request):
    if "email" in request.session:
        uid = User.objects.get(email=request.session['email'])
        cid = Chairman.objects.get(user_id = uid)
        if request.POST:
            title = request.POST['title']
            amount = request.POST['amount']
            duedate = request.POST['duedate']

            sall = Societymember.objects.all()
            for i in sall:
                sid = Societymember.objects.get(id = i.id)
                print("===================------------------>>",sid)
                mid = Maintainance.objects.create(user_id = uid,member_id = sid,title=title,amount=amount,duedate=duedate)
                #send_mail("MAINTAINANCE : ",mid.title,"shirinshaikh241020@gmail.com",[i.member_id.user_id.email])
        context = {
            'status' : "Successfully Added....",
            'uid' : uid,
            'cid' : cid,
        }
        return render(request,"chairmanapp/add-maintainance.html",context) 
    context = { 
                'uid' : uid,
                'cid' : cid,
            }
    return render(request,"chairmanapp/add-maintainance.html",context) 

def all_maintainance(request):   
     if "email" in request.session:
        uid = User.objects.get(email=request.session['email'])
        cid = Chairman.objects.get(user_id = uid)

        mall = Maintainance.objects.all()
        total = 0
        for i in mall:
            total+= int(i.amount)
        context = { 
                'uid' : uid,
                'cid' : cid,
                'mall' : mall,
                'total' : total,
            }
        return render(request,"chairmanapp/all-maintainance.html",context) 
     
def register(request):
    if request.POST:
        role=request.POST['role']
        if role=="chairman":
            email=request.POST['email']
            print("===========email", email)
            password=request.POST['password']
            print("===========password", password)
            firstname=request.POST['firstname']
            print("===========firstname", firstname)
            lastname=request.POST['lastname']
            print("===========lastname", lastname)
            contact_no=request.POST['contactno']
            print("===========contact", contact_no)
            isactive="True"
            isvarify = "True"

            uid=User.objects.create(user_id=uid,email=email,password=password,is_varify=isvarify,is_active=isactive,role=role,otp="1234",created_at="not provided",updated_at="not provided")
            uid.save()
            cid=User.objects.create(firstname=firstname,lastname=lastname,contact_no=contact_no)
            cid.save()
            smsg="Added Successfully"
            context={
                    'uid':uid,
                    'cid':cid,
                    'smsg':smsg,
                    }
            
            return render(request,"chairmanapp/register.html",context)
        else:
            if role=="societymember":
                email=request.POST['email']
                password=request.POST['password']
                firstname=request.POST['firstname']
                lastname=request.POST['lastname']
                contact_no=request.POST['contact_no']
                isactive="True"
                isvarify = "True"

                uid=User.objects.create(user_id=uid,email=email,password=password,is_varify=isvarify,is_active=isactive,role=role,otp="1234",created_at="not provided",updated_at="not provided")
                sid=Societymember.objects.create(firstname=firstname,lastname=lastname,contact_no=contact_no)

                uid.save()

                smsg="Added Successfully"
                context={
                        'uid':uid,
                        'sid':sid,
                        'smsg':smsg,
                        }
                # sendmail
                
                return render(request,"societymemberapp/register.html",context)
    else:
        return render(request,"chairmanapp/register.html")


     
def add_event(request):
    if "email" in request.session:
        uid = User.objects.get(email=request.session['email'])
        cid = Chairman.objects.get(user_id = uid)
        if request.POST:
            eid = Event.objects.create(
                 user_id = uid,
                 title = request.POST['title'],
                 description = request.POST['description']

            )
            eall = Event.objects.all()
            context = {
                    'uid' : uid,
                    'cid' : cid,
                    'eall' : eall,
                }
            return render(request,"chairmanapp/event-list.html",context)
        else:
            context = {
                        'uid' : uid,
                        'cid' : cid,
                    }
            return render(request,"chairmanapp/add-event.html",context)
    else:
        return redirect("login")
    
def view_event(request):
    if "email" in request.session:
        uid = User.objects.get(email=request.session['email'])
        cid = Chairman.objects.get(user_id = uid)
        eall = Event.objects.all()
        context = {
                    'uid' : uid,
                    'cid' : cid,
                    'eall' : eall,
                }
        return render(request,"chairmanapp/event-list.html",context)
    else:
        return redirect("login")
    
def view_event_details(request,pk):
    if "email" in request.session:
        print("----------------------->PK",pk)
        uid = User.objects.get(email=request.session['email'])
        cid = Chairman.objects.get(user_id = uid)
        event = Event.objects.filter(id = pk)
        context = {
                    'uid' : uid,
                    'cid' : cid,
                    'event' : event,
                }
        return render(request,"chairmanapp/event-details.html",context)
    else:
        return redirect("login")   
def add_complain(request):
    if "email" in request.session:
        uid = User.objects.get(email=request.session['email'])
        cid = Chairman.objects.get(user_id = uid)
        if request.POST:
            if "picture" in request.FILES:
                     cid.pic_complain = request.FILES['picture']
            cid.save()
            co_id = Complain.objects.create(
                 user_id = uid,
                 title = request.POST['title'],
                 description = request.POST['description']

                

            )
            call = Complain.objects.all()
            context = {
                    'uid' : uid,
                    'cid' : cid,
                    'call' : call,
                }
            return render(request,"chairmanapp/complain-list.html",context)
        else:
            context = {
                        'uid' : uid,
                        'cid' : cid,
                    }
            return render(request,"chairmanapp/add-complain.html",context)
    else:
        return redirect("login")
    
def view_complain(request):
    if "email" in request.session:
        uid = User.objects.get(email=request.session['email'])
        cid = Chairman.objects.get(user_id = uid)
        call = Complain.objects.all()
        context = {
                    'uid' : uid,
                    'cid' : cid,
                    'call' : call,
                }
        return render(request,"chairmanapp/complain-list.html",context)
    else:
        return redirect("login")
    
def view_complain_details(request,pk):
    if "email" in request.session:
        print("----------------------->PK",pk)
        uid = User.objects.get(email=request.session['email'])
        cid = Chairman.objects.get(user_id = uid)
        complain = Complain.objects.filter(id = pk)
        context = {
                    'uid' : uid,
                    'cid' : cid,
                    'complain' : complain,
                }
        return render(request,"chairmanapp/complain-details.html",context)
    else:
        return redirect("login")   
    

