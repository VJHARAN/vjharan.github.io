from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from users.forms import profileUpdateForm, userUpdateForm
from users.models import Profile as Pro
from users.models import Requests
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from django.core.mail import EmailMessage

@login_required
def Profile(request):
    if request.method == 'POST':
        u_form = userUpdateForm(request.POST,instance=request.user)
        p_form = profileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your account has been successfully updated!')
            return redirect('users:profile')
    else:
        u_form = userUpdateForm(instance=request.user)
        p_form = profileUpdateForm(instance=request.user.profile)

    context= {
        'u_form':u_form,
        'p_form':p_form,
        # 'user_membership':user_membership,
        # 'user_subscription': user_subscription
    }
    return render(request,'profile/profile.html',context)


def Request(request):
    if request.method == 'POST':
        name= request.POST.get('name')
        email = request.POST.get('e-mail')
        tel_number = request.POST.get('phone')
        prof = request.user.profile
        Request = Requests(profile=prof,name=name, email=email, tel_number=tel_number)
        Request.save()
        prof_id = prof.id
        Pro.objects.filter(id=prof_id).update(is_teacher=True)
        
        message = 'Your request for a teacher account has been accepted! Now you can go back to LearnOn and upload courses and lectures, good job!'
        send_mail(
            'LearnOn, the request was accepted.',
            message,
            'LearnOn@no-reply.com',
            [email],
            fail_silently=False,
        )
        send_mail(
            'LearnOn',
            'Someone requested a teacher account. With info: ' + name + ' , ' + email + ' , ' + tel_number + ' , ' + str(prof) + '.',
            'LearnOn@no-reply.com',
            ['redian1marku@gmail.com'],
            fail_silently=False,
        )
        messages.info(request, f'The request was sent successfully, you will be notified by email.')
        return redirect('courses:home')


