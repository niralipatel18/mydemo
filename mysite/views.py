from django.shortcuts import render,HttpResponse,redirect,Http404
from .models import signup,post,reviews
from .forms import signupform,postform,reviewsform
from demo import settings 
from django.core.mail import send_mail
from django.contrib.auth import authenticate,logout
from django.contrib.sessions.models import Session
import random


#Create your views here.
def index(request):
    user=request.session.get('email')
    if request.method =='POST':
        myfrm=signupform(request.POST)
        if myfrm.is_valid():
            myfrm.save()
            
            #send mail
            otp=random.randint(111111,999999)
            subject='Django Testing Mail'
            msg=f"Well come to nirali dobariya's testing site ,please enjoy our services, Your account has been created successfully! your one time password is:{otp}"
            from_id=settings.EMAIL_HOST_USER
            to_id=[myfrm.cleaned_data.get('email')]  
            send_mail(subject,msg,from_id,to_id)

            print("signup successfully")
            return redirect('/login')
        else:
            print(myfrm.errors)
    else:
        myfrm=signupform()
    return render(request, 'index.html',{'myfrm':myfrm,'user':user})

    

def login(request):
    if request.method =='POST':
        if request.POST.get('login')=='login':
            email=request.POST['email']
            password=request.POST['password']
            u_id=signup.objects.get(email=email)
            #login_check=authenticate(username=unm,password=pas)
            user=signup.objects.filter(email=email,password=password)
        
            if user:
                request.session['email'] = email
                request.session['u_id'] =u_id.id
                # print("successfully..!")
                return redirect('/about')
            else:
                print("incorrct username or password...")
        else:
            myfrm=signupform(request.POST)
            if myfrm.is_valid():
                myfrm.save()
            
                #send mail
                otp=random.randint(111111,999999)
                subject='Django Testing Mail'
                msg=f"Well come to nirali dobariya's testing site ,please enjoy our services, Your account has been created successfully! your one time password is:{otp}"
                from_id=settings.EMAIL_HOST_USER
                to_id=[myfrm.cleaned_data.get('email')]  
                send_mail(subject,msg,from_id,to_id)

                print("signup successfully")
                return redirect('/login')
            else:
                print(myfrm.errors)

    else:
        print("not login")

    return render(request, 'login.html')

def about(request):
    user=request.session.get('email')
    if request.method =='POST':
        myfrm=signupform(request.POST)
        if myfrm.is_valid():
            myfrm.save()
            
            #send mail
            otp=random.randint(111111,999999)
            subject='Django Testing Mail'
            msg=f"Well come to nirali dobariya's testing site ,please enjoy our services, Your account has been created successfully! your one time password is:{otp}"
            from_id=settings.EMAIL_HOST_USER
            to_id=[myfrm.cleaned_data.get('email')]  
            send_mail(subject,msg,from_id,to_id)

            print("signup successfully")
            return redirect('/login')
        else:
            print(myfrm.errors)
    else:
        myfrm=signupform()
    return render(request, 'about.html',{'myfrm':myfrm,'user':user})

def contact(request):
    user=request.session.get('email')
    if request.method =='POST':
        myfrm=signupform(request.POST)
        if myfrm.is_valid():
            myfrm.save()
            
            #send mail
            otp=random.randint(111111,999999)
            subject='Django Testing Mail'
            msg=f"Well come to nirali dobariya's testing site ,please enjoy our services, Your account has been created successfully! your one time password is:{otp}"
            from_id=settings.EMAIL_HOST_USER
            to_id=[myfrm.cleaned_data.get('email')]  
            send_mail(subject,msg,from_id,to_id)

            print("signup successfully")
            return redirect('/login')
        else:
            print(myfrm.errors)
    else:
        myfrm=signupform()
    return render(request, 'contact.html',{'myfrm':myfrm,'user':user})


def profile(request):
    return render(request,'profile.html')
    
    # if request.session.has_key('email'):
    #     s_data=signup.objects.all()
    #     user=request.session.get('email')
    #     return render(request,'profile.html',{'s_data':s_data,'user':user})
    # else:
    #     return redirect('/login')
    

        

def update(request,id):
    user=request.session.get('email')

    if request.method == 'POST':
        myfrm1=signupform(request.POST)
        id=signup.objects.get(id=id)
        if myfrm1.is_valid():
            myfrm1=signupform(request.POST,instance=id)
            myfrm1.save()
            return redirect('/profile')
        else:
            print(myfrm1.errors)
    else:
        myfrm1=signupform()
    return render(request, 'update.html',{'myfrm1':myfrm1,'signupdata':signup.objects.get(id=id),'user':user})

def delete(request,id):
    sid=signup.objects.get(id=id)
    sid.delete()
    return redirect('/profile')

def logout(request):
    try:
         del request.session['email']
    except:
          pass
    finally:
        return redirect('/')

def profile_update(request):
    user=request.session.get('email')

    u_id=request.session.get('u_id')
    user_id=request.session.get('email')
    if request.method =='POST':
        #myfrm=signupform(request.POST)
        id=signup.objects.get(id=u_id)
        myfrm=signupform(request.POST,instance=id)
        if myfrm.is_valid():
            myfrm.save()
            return redirect('/')
        else:
            print(myfrm.errors)
    else:
        myfrm=signupform()

    return render(request, 'profile_update.html',{'myfrm': myfrm,'u_data':signup.objects.get(id=u_id),'user_id':user_id,'user':user})




def post_form(request):
    if request.session.has_key('email'):
        user=request.session.get('email')
        if request.method =='POST':

            p_frm=postform(request.POST,request.FILES)
            if p_frm.is_valid():
                p_frm.save()
                print("data uploaded successfully")
                return redirect('/view_post')
            else:
             print(p_frm.errors)

        else:
            p_frm=postform()
        return render(request, 'post_form.html',{'p_frm':p_frm,'user':user})

    else:
        return redirect('/login')

def view_post(request):
    if request.session.has_key('email'):
        data=post.objects.all()
        user=request.session.get('email')
        return render(request, 'view_post.html',{'data':data,'user':user})
    else:
        return redirect('/login')

    

'''def update_post(request,id):
    if request.method == 'POST':
        myfrm1=signupform(request.POST)
        id=signup.objects.get(id=id)
        if myfrm1.is_valid():
            myfrm1=signupform(request.POST,instance=id)
            myfrm1.save()
            return redirect('/profile')
        else:
            print(myfrm1.errors)
    else:
        myfrm1=signupform()
    return render(request, 'update.html'{'myfrm1':myfrm1,'signupdata':signup.objects.get(id=id)})
'''

def update_post(request,id):
    if request.method =='POST':
        p_frm=postform(request.POST,request.FILES)
        id=post.objects.get(id=id)
        if p_frm.is_valid():
            p_frm=postform(request.POST,request.FILES,instance=id)
            p_frm.save()
            return redirect('/view_post')
        else:
            print(p_frm.errors)
    else:
        p_frm=postform()
    return render(request,'update_post.html',{'p_frm':p_frm,'postdata':post.objects.get(id=id)})

def delete_post(request,id):
    pid=post.objects.get(id=id)
    pid.delete()
    return redirect('/view_post')


def review(request):
    if request.session.has_key('email'):
        data=reviews.objects.all()
        user=request.session.get('email')
        if request.method == 'POST':
            r_frm=reviewsform(request.POST)
            print('Review inserted successfully')

            if r_frm.is_valid():
                r_frm.save()
                print('Review inserted successfully')
                return redirect('/')
            else:
                print(r_frm.errors)
        else:
            r_frm=reviewsform()
        return render(request,'review.html',{'user':user,'r_frm':r_frm,'data':data})
    else:
        return redirect('/login')

def exchange(request):
    return render(request,"exchange.html")

                

#subject = 'welcome to GFG world'
#message = 'Hi, thank you for registering in geeksforgeeks.'
#email_from = settings.EMAIL_HOST_USER 
#recipient_list =['nehal.pan17@gmail.com'] 
#send_mail( subject, message, email_from, recipient_list ) 