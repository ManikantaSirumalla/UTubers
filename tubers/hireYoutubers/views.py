from django.shortcuts import redirect, render
from .models import HireYoutubers


# Create your views here.
from django.contrib import messages


def hireYoutubers(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        utuber_id = request.POST['utuber_id']
        utuber_name = request.POST['utuber_name']
        city = request.POST['city']
        phone = request.POST['phone']
        email = request.POST['email']
        state = request.POST['state']
        message = request.POST['message']
        user_id = request.POST['user_id']

        # TODO: do all sanitization
        hireYoutubers = HireYoutubers(first_name=first_name, last_name=last_name, utuber_id=utuber_id, utuber_name=utuber_name,
                              city=city, phone=phone, email=email, state=state, message=message, user_id=user_id)
        hireYoutubers.save()
        messages.success(request, 'Thanks for reaching out!')
        return redirect('youtubers')
