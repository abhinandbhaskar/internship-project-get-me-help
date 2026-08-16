import datetime
import email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render
from myapp.models import login, user, work_request, complaints, bank
from myapp.models import worker,own_services,feed_backs,services
# Create your views here.

from myapp.models import PaymentStatus

def main_page(request):
    return render(request,'index.html')

def adminn_home_page(request):
    return render(request,'admin/admin_homepage.html')

def user_home_page(request):
    return render(request,'user/user_homepage.html',{"id":id})

def worker_home_page(request):
    return render(request,'worker/worker_homepage.html',{"id":id})

def login_page(request):
    return render(request,'login_page.html')


def loginn_post(request):
    username=request.POST['username']
    password=request.POST['password']
    # print(username,password)
    res=login.objects.filter(username=username,password=password)
    if res.exists():
        res=res[0]
        request.session['lid']=res.id
        if res.usertype=="admin":
            return HttpResponse("<script>alert('Login successfull');window.location='/home_page_adm'</script>")
        elif res.usertype=="worker":
            return HttpResponse("<script>alert('Login successfull');window.location='/worker_home_page'</script>")
        elif res.usertype=='user':
            return HttpResponse("<script>alert('Login successfull');window.location='/user_home_page'</script>")
        else:
            return HttpResponse("<script>alert('Waiting for admin approval..');window.location='/'</script>")
    else:
        return HttpResponse("<script>alert('username and password doesnot exist...');window.location='/'</script>")




# user functions sections##########################################################

def main_registration(request):
    return render(request,'main_reg.html')


def user_reg(request):
    return render(request,'user/userreg.html')

def user_reg_post(request):
    name=request.POST['name']
    place=request.POST['place']
    pin=request.POST['pin']
    post=request.POST['post']
    email=request.POST['email']
    phone=request.POST['phone']
    password=request.POST['password']
    res=login.objects.filter(username=email)
    if res.exists():
        return HttpResponse("<script>alert('username already exists...');window.location='/main_registration';</script>")
    if 'image' in request.FILES:
        image = request.FILES['image']
        dt = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        fs = FileSystemStorage()
        fs.save(r"C:\Users\abhin\PycharmProjects\get_me_help\myapp\static\images\\" + dt + ".jpg", image)
        path = "/static/images/" + dt + ".jpg"
    else:
        path="/static/page_templates/images/dfimage.jpg"
    obj1=login()
    obj1.username=email
    obj1.password=password
    obj1.usertype="user"
    obj1.save()
    obj=user()
    obj.name=name
    obj.place=place
    obj.pin=pin
    obj.post=post
    obj.email=email
    obj.phone=phone
    obj.image=path
    obj.LOGIN=obj1
    print(obj1)
    obj.save()
    return HttpResponse("<script>alert('user registration successfull');window.location='/';</script>")

def view_user_profile(request):
    obj=user.objects.get(LOGIN=request.session['lid'])
    return render(request,'user/view_userprofile.html',{"data":obj})

def add_bank_account(request):
    return render(request,'user/add_user_bankacct.html')

def add_bank_account_post(request):
    bankname=request.POST['bankname']
    acctno=request.POST['acctno']
    ifsccode=request.POST['ifsccode']
    branch=request.POST['branchname']
    balance=request.POST['balance']
    res = bank.objects.filter(LOGIN_id=request.session['lid'])
    res=len(res)
    res1= bank.objects.filter(LOGIN_id=request.session['lid'],bank_name=bankname)
    if res1.exists():
        return HttpResponse("<script>alert('Same Bank Details Already Added..');window.location='/user_home_page';</script>")
    if res==2:
        return HttpResponse("<script>alert('You can add only 2 bank details..');window.location='/user_home_page';</script>")
    else:
        obj = bank()
        obj.bank_name = bankname
        obj.accnt_no = acctno
        obj.ifsc_code = ifsccode
        obj.branch_name = branch
        obj.balance = balance
        obj.LOGIN = login.objects.get(id=request.session['lid'])
        obj.save()
        return HttpResponse("<script>alert('Bank details added..');window.location='/user_home_page';</script>")


def view_ubank_details(request):
    res = bank.objects.filter(LOGIN_id=request.session['lid'])
    return render(request,'user/view_uaccount_details.html',{"data":res})

def user_dlt_bank_dts(request,id):
    bank.objects.get(id=id).delete()
    return HttpResponse("<script>alert('Bank details deleted..');window.location='/view_ubank_details#next';</script>")

def user_upt_bank_dts(request,id):
    res=bank.objects.get(id=id)
    return render(request,'user/update_user_bnk_acnt.html',{"data":res})


def user_upt_bank_dts_post(request,id):
    bankname = request.POST['bankname']
    acctno = request.POST['acctno']
    ifsccode = request.POST['ifsccode']
    branch = request.POST['branchname']
    balance = request.POST['balance']
    bank.objects.filter(id=id).update(bank_name=bankname,accnt_no=acctno,ifsc_code=ifsccode,branch_name=branch,balance=balance)
    return HttpResponse("<script>alert('bank details updated');window.location='/view_ubank_details#next';</script>")







def edit_user_profile(request,id):
    obj=user.objects.get(id=id)
    return render(request,'user/edit_user_profile.html',{"data":obj})

def edit_user_profile_post(request,id):
    name = request.POST['name']
    place = request.POST['place']
    pin = request.POST['pin']
    post = request.POST['post']
    email = request.POST['email']
    phone = request.POST['phone']
    if 'image' in request.FILES:
        image = request.FILES['image']
        dt = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        fs = FileSystemStorage()
        fs.save(r"C:\Users\abhin\PycharmProjects\get_me_help\myapp\static\images\\" + dt + ".jpg", image)
        path = "/static/images/" + dt + ".jpg"
        user.objects.filter(LOGIN_id=request.session['lid']).update(image=path)
    user.objects.filter(id=id).update(name=name,place=place,pin=pin,post=post,email=email,phone=phone)
    return HttpResponse("<script>alert('user profile updated');window.location='/view_user_profile#next';</script>")





def view_workers_services(request):
    obj=own_services.objects.all()
    return render(request,'user/view_workers_services.html',{"data":obj})


def addworker_bnk_dtls(request):
    return render(request,'worker/add_woker_bankacct.html')

def addworker_bnk_dtls_post(request):
    bankname = request.POST['bankname']
    acctno = request.POST['acctno']
    ifsccode = request.POST['ifsccode']
    branch = request.POST['branchname']
    balance = request.POST['balance']
    res=bank.objects.filter(LOGIN_id=request.session['lid']).count()
    # return render(request,'worker/values.html',{"data":res})
    if res==1:
        return HttpResponse("<script>alert('You can only add one bank account to your payment section.');window.location='/worker_home_page';</script>")
    else:
        obj = bank()
        obj.bank_name=bankname
        obj.accnt_no=acctno
        obj.ifsc_code=ifsccode
        obj.branch_name=branch
        obj.balance=balance
        obj.LOGIN=login.objects.get(id=request.session['lid'])
        obj.save()
        return HttpResponse("<script>alert('bank details submited');window.location='/addworker_bnk_dtls';</script>")

def change_user_pass(request):
    return render(request, 'user/changepassword.html')

def change_user_pass_post(request):
    obj = login.objects.get(id=request.session['lid'])
    currentpassword = request.POST['currentpassword']
    newpassword = request.POST['newpassword']
    confirmpassword = request.POST['confirmpassword']
    res = obj.password
    if res != currentpassword:
        return HttpResponse("<script>alert('Your current password is not correct..');window.location='/change_user_pass#next';</script>")
    if newpassword != confirmpassword:
        return HttpResponse("<script>alert('New password and confirm password enter correctly...');window.location='/change_user_pass#next';</script>")
    login.objects.filter(id=request.session['lid']).update(password=newpassword)
    return HttpResponse("<script>alert('password updated..');window.location='/change_user_pass#next';</script>")


def view_worker_baccnt(request):
    res=bank.objects.filter(LOGIN=request.session['lid'])
    return render(request,'worker/view_workaccount_details.html',{"data":res})

def worker_upt_bank_dts(request,id):
    res=bank.objects.get(id=id)
    return render(request,'worker/update_woker_bankacct.html',{"data":res})


def worker_upt_bank_dts_post(request,id):
    bankname = request.POST['bankname']
    acctno = request.POST['acctno']
    ifsccode = request.POST['ifsccode']
    branch = request.POST['branchname']
    balance = request.POST['balance']
    bank.objects.filter(id=id).update(bank_name=bankname,accnt_no=acctno,ifsc_code=ifsccode,branch_name=branch,balance=balance)
    return HttpResponse("<script>alert('bank details updated');window.location='/view_worker_baccnt#next';</script>")



def worker_dlt_bank_dts(request,id):
    bank.objects.get(id=id).delete()
    return HttpResponse("<script>alert('bank details deleted.');window.location='/view_worker_baccnt#next';</script>")



def user_work_request(request,id):
    obj1 = own_services.objects.get(id=id)
    obj=work_request()
    dt = datetime.datetime.now().strftime("%Y/%m/%d")
    obj.date=dt
    obj.status="pending"
    obj.USER=user.objects.get(LOGIN__id=request.session['lid'])
    obj.OWNSERVICES=obj1
    obj.save()
    return HttpResponse("<script>alert('request submited');window.location='/view_workers_services#next';</script>")






def view_wrk_request_sts(request):
    obj=work_request.objects.filter(USER__LOGIN=request.session['lid'])
    return render(request,'user/View_wrk_reqst_sts.html',{"data":obj})

def payment_selection(request,id,amnt):
    request.session['wid']=id
    obj = work_request.objects.filter(USER__LOGIN=request.session['lid'])
    res1=bank.objects.filter(LOGIN=request.session['lid'])
    return render(request,'user/payment_selection.html',{"data2":res1,"data3":obj,"amnt":amnt})


def make_payment(request,eid,amnt):
    res=bank.objects.get(id=eid)
    res1=bank.objects.get(id=eid).LOGIN_id
    name=user.objects.get(LOGIN_id=res1).name
    obj = work_request.objects.get(id=request.session['wid'])
    return render(request,'user/payment_page.html',{"data":res,"data3":obj,"amnt":amnt,"name":name})



def make_payment_post(request):
    obj = work_request.objects.get(id=request.session['wid'])
    price_value=obj.OWNSERVICES.amount
    price=int(price_value)
    re=PaymentStatus()
    bnkname=request.POST['bankname']
    re.bankname=bnkname
    res = bank.objects.get(LOGIN_id=request.session['lid'], bank_name=bnkname)
    date=datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    re.date=date
    re.paymnt_sts="payment completed"
    re.OWNSERVICES_id=obj.OWNSERVICES.id
    re.USER_id=obj.USER.id
    balance=res.balance
    balance_value=int(balance)
    if balance_value < price:
        return HttpResponse("<script>alert('Insufficient cash ');window.location='/view_wrk_request_sts#next';</script>")
    re.save()
    # res = bank.objects.get(LOGIN_id=request.session['lid'],bank_name=bnkname)
    new_amount=int(res.balance)-int(obj.OWNSERVICES.amount)
    bank.objects.filter(LOGIN=request.session['lid'],bank_name=bnkname).update(balance=new_amount)
    res11 = bank.objects.get(LOGIN=obj.OWNSERVICES.WORKER.LOGIN.id)
    w_balance=res11.balance
    w_new_balane=int(w_balance)+int(obj.OWNSERVICES.amount)
    bank.objects.filter(LOGIN=obj.OWNSERVICES.WORKER.LOGIN.id).update(balance=w_new_balane)
    return HttpResponse("<script>alert('Payment Successfull');window.location='/view_wrk_request_sts#next';</script>")



def prevoius_works(request):
    res=work_request.objects.filter(USER__LOGIN=request.session['lid'],status="approve")
    return render(request,'user/previous_works.html',{"data":res})


def payment_status(request):
    obj=PaymentStatus.objects.filter(USER__LOGIN_id=request.session['lid'])
    return render(request,'user/payment_status.html',{"data":obj})


def snd_feedback(request,id):
    return render(request,'user/snd_feedback.html',{"id":id})

def snd_feedback_post(request,id):
    feedback=request.POST['feedback']
    obj1=feed_backs()
    obj=user.objects.get(LOGIN__id=request.session['lid'])
    dt=datetime.datetime.now().strftime('%Y/%m/%d')
    obj1.feedback = feedback
    obj1.date=dt
    obj1.USER_id=obj.id
    obj1.WORKER=worker.objects.get(id=id)
    obj1.save()
    return HttpResponse("<script>alert('feedback submited...');window.location='/user_home_page';</script>")


def snd_complaint(request):
    return render(request,'user/snd_complaints.html')


def snd_complaint_post(request):
    cmpt=request.POST['complaint']
    res=user.objects.get(LOGIN=request.session['lid'])
    dt=datetime.datetime.now().strftime("%Y/%m/%d")
    obj=complaints()
    obj.complaint=cmpt
    obj.date=dt
    obj.reply="pending"
    obj.reply_date="pending"
    obj.USER=res
    obj.save()
    return HttpResponse("<script>alert('complaint submited');window.location='/view_complaint_reply#next';</script>")

def view_complaint_reply(request):
    obj=complaints.objects.filter(USER__LOGIN=request.session['lid'])
    return render(request,'user/view_cmplt_reply.html',{"data":obj})







#admin section functions//////////////////////////////////

def view_registered_workers(request):
    obj=worker.objects.filter(LOGIN__usertype="pending")
    return render(request,'admin/View_registered_workers.html',{"data":obj})

def reject_worker(request,id):
    import smtplib
    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login("getmehelp608@gmail.com", "uzuy ayhk ohic hknj")
    msg = MIMEMultipart()  # create a message.........."
    msg['From'] = "getmehelp608@gmail.com"
    worker = login.objects.get(id=id)
    email = worker.username
    msg['To'] = email
    msg['Subject'] = " Getmehelp Job Searching Website "
    body = "Sorry!: Email:" + str(email)+" There are some issues in your registration You are rejected..."
    msg.attach(MIMEText(body, 'plain'))
    s.send_message(msg)
    login.objects.get(id=id).delete()
    return HttpResponse("<script>alert('deleted');window.location='/view_registered_workers#next';</script>")


def approve_worker(request,id):
    login.objects.filter(id=id).update(usertype="worker")
    import smtplib
    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login("getmehelp608@gmail.com", "uzuy ayhk ohic hknj")
    msg = MIMEMultipart()  # create a message.........."
    msg['From'] = "getmehelp608@gmail.com"
    worker=login.objects.get(id=id)
    email=worker.username
    password=worker.password
    msg['To'] = email
    msg['Subject'] = "Your Password for Getmehelp Website"
    body = "Congratulations! You have been approved as a worker on the Getmehelp Website.Your Password is:" +str(password)+ " Email:"+ str(email)
    msg.attach(MIMEText(body, 'plain'))
    s.send_message(msg)
    return HttpResponse("<script>alert('approved..');window.location='/view_registered_workers#next';</script>")




def view_approved_workers(request):
    obj=worker.objects.filter(LOGIN__usertype='worker')
    return render(request,'admin/View_approved_workers.html',{"data":obj})


def view_users(request):
    obj=user.objects.all()
    return render(request,'admin/view_users.html',{"data":obj})

def view_cmplt_snd_reply(request):
    obj=complaints.objects.all()
    return render(request,'admin/view_cmplt_snd_rly.html',{"data":obj})

def snd_replys(request,id):
    return render(request,'admin/send_reply.html',{"id":id})

def snd_reply_post(request,id):
    reply=request.POST['replay']
    dt=datetime.datetime.now().strftime("%Y/%m/%d")
    complaints.objects.filter(id=id).update(reply=reply,reply_date=dt)
    return HttpResponse("<script>alert('replayed..');window.location='/view_cmplt_snd_reply#next';</script>")

def view_feedbacks(request):
    obj=feed_backs.objects.all()
    return render(request,'admin/View_feedback.html',{"data":obj})

def add_services(request):
    return render(request,'admin/Add_services.html')

def add_service_post(request):
    service = request.POST['services']
    res = services.objects.filter(service_name=service)
    if res.exists():
        return HttpResponse("<script>alert('servicename is already exists');window.location='/add_services#next'</script>")
    obj = services()
    obj.service_name = service
    obj.save()
    return HttpResponse("<script>alert('Service added..');window.location='view_user_services#next';</script>")

def view_user_services(request):
    obj=services.objects.all()
    return render(request,'admin/View_services.html',{"data":obj})

def delete_services(request,id):
    services.objects.get(id=id).delete()
    return HttpResponse("<script>alert('service deleted..');window.location='/view_user_services#next'</script>")


def payment_report(request):
    res=PaymentStatus.objects.filter(paymnt_sts="payment completed")
    sum=0
    for i in res:
        sum=sum+int(i.OWNSERVICES.amount)
    return render(request,'admin/payment_report.html',{"data":res,"total":sum})


def change_admin_pass(request):
    return render(request,'admin/changepassword.html')

def change_admin_pass_post(request):
    obj=login.objects.get(id=request.session['lid'])
    currentpassword=request.POST['currentpassword']
    newpassword=request.POST['newpassword']
    confirmpassword=request.POST['confirmpassword']
    res=obj.password
    if res != currentpassword:
        return HttpResponse("<script>alert('Your current password is not correct..');window.location='/change_admin_pass#next';</script>")
    if newpassword!=confirmpassword:
        return HttpResponse("<script>alert('New password and confirm password enter correctly...');window.location='/change_admin_pass#next';</script>")
    login.objects.filter(id=request.session['lid']).update(password=newpassword)
    return HttpResponse("<script>alert('password updated..');window.location='/';</script>")









#worker section functions//////////////////////////////////


def worker_reg(request):
    return render(request, 'worker/workerreg.html')


def worker_reg_post(request):
    name=request.POST['name']
    email=request.POST['email']
    phone=request.POST['phone']
    img=request.FILES['image']
    password=request.POST['password']
    dt=datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    fs=FileSystemStorage()
    fs.save(r"C:\Users\abhin\PycharmProjects\get_me_help\myapp\static\images\\"+dt+".jpg",img)
    path="/static/images/"+dt+".jpg"
    res=login.objects.filter(username=email)
    if res.exists():
        return HttpResponse("<script>alert('username already exists.');window.location='/worker_reg';</script>")
    obj1=login()
    obj1.username=email
    obj1.password=password
    obj1.usertype="pending"
    obj1.save()
    obj=worker()
    obj.worker_name=name
    obj.email = email
    obj.phone=phone
    obj.image=path
    # obj.LOGIN_id=obj1.id
    obj.LOGIN=obj1
    obj.save()
    return HttpResponse("<script>alert('Registration successfull..');window.location='/';</script>")

def worker_profile(request):
    obj=worker.objects.get(LOGIN__id=request.session['lid'])
    # print(obj.image,"hgh")
    return render(request,'worker/View_worker_profile.html',{"data":obj})

def edit_wrkr_profile(request,id):
    obj = worker.objects.get(id = id)
    return render(request,'worker/edit_wrkr_profile.html',{"data":obj})

def edit_wrkr_profile_post(request,id):
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    if 'image' in request.FILES:
        img = request.FILES['image']
        dt = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        fs = FileSystemStorage()
        fs.save(r"C:\Users\abhin\PycharmProjects\get_me_help\myapp\static\images\\" + dt + ".jpg", img)
        path = "/static/images/" + dt + ".jpg"
        worker.objects.filter(LOGIN_id=request.session['lid']).update(image=path)
    worker.objects.filter(id=id).update(worker_name=name,email=email,phone=phone)
    return HttpResponse("<script>alert('Profile Updated..');window.location='/worker_profile#next';</script>")

def view_services(request):
    obj=services.objects.all()
    return render(request,'worker/view_services.html',{"data":obj})

def add_own_services(request,id):
    res=services.objects.get(id=id)
    return render(request,'worker/add_own_service.html',{"data":res})

def add_own_srv_post(request,id):
    amount=request.POST['amount']
    obj=own_services()
    obj.amount=amount
    obj.SERVICE_id=id
    obj.WORKER=worker.objects.get(LOGIN=request.session['lid'])
    obj.save()
    return HttpResponse("<script>alert('Amount added');window.location='/view_own_services#next';</script>")







def view_own_services(request):
    obj=own_services.objects.filter(WORKER__LOGIN=request.session['lid'])
    return render(request,'worker/own_services.html',{"data":obj})

def delete_own_services(request,id):
    own_services.objects.get(id=id).delete()
    return HttpResponse("<script>alert('Deleted..');window.location='/view_own_services#next';</script>")


def view_user_request(request):
    obj=work_request.objects.filter(OWNSERVICES__WORKER__LOGIN=request.session['lid'])
    return render(request,'worker/view_user_request.html',{"data":obj})


def payments(request):
    obj=PaymentStatus.objects.filter(OWNSERVICES_id__WORKER__LOGIN__id=request.session['lid'])
    sum=0
    val=0
    for i in obj:
        val=int(i.OWNSERVICES.amount)
        sum=sum+val
    return render(request,'worker/payments.html',{"data":obj,"total":sum})


def request_approve(request,id):
    work_request.objects.filter(id=id).update(status="approve")
    return HttpResponse("<script>alert('approved..');window.location='/view_user_request#next';</script>")

def reject_request(request,id):
    work_request.objects.filter(id=id).update(status="rejected")
    return HttpResponse("<script>alert('rejected..');window.location='/view_user_request#next';</script>")





def view_feedback(request):
    obj=feed_backs.objects.filter(WORKER__LOGIN=request.session['lid'])
    return render(request,'worker/View_feedbacks.html',{"data":obj})



def change_worker_pass(request):
    return render(request,'worker/changepassword.html')

def change_worker_pass_post(request):
    obj=login.objects.get(id=request.session['lid'])
    currentpassword=request.POST['currentpassword']
    newpassword=request.POST['newpassword']
    confirmpassword=request.POST['confirmpassword']
    res=obj.password
    if res != currentpassword:
        return HttpResponse("<script>alert('Your current password is not correct..');window.location='/change_worker_pass#next';</script>")
    if newpassword!=confirmpassword:
        return HttpResponse("<script>alert('New password and confirm password enter correctly...');window.location='/change_worker_pass#next';</script>")
    login.objects.filter(id=request.session['lid']).update(password=newpassword)
    return HttpResponse("<script>alert('password updated..');window.location='/';</script>")


