from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import Message
from accounts.models import User


def index(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    else:
        message = Message.objects.all()
        users = User.objects.all()
        context = {
            'first_name': users,
            'chat': message,
        }
        return render(request, "chat_room/index.html", context)


def post(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    else:
        if request.method == "POST":
            msg = request.POST.get('msgbox', None)
            user = Message(user=request.user, message=msg)
            user.receiver = request.GET.get('r', '')
            if msg != '':
                user.save()
            elif user.receiver == '':
                msg = "Please select a person from your contact list to start your chat!"
                return render(request, 'chat_room/index.html', {'msg': msg})
            message_ids1 = []
            for message in Message.objects.filter(receiver=user.receiver):
                message_ids1.append(message.pk)
            user_message1 = Message.objects.filter(pk__in=message_ids1)
            context = {
                'msg': user_message1,
                'user': user.user.username,
                'receiver': user.receiver,
            }
            return JsonResponse(context)
        else:
            return HttpResponse('Request must be POST.')


def messages(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    else:
        message = Message.objects.all()
        return render(request, 'chat_room/messages.html', {'chat': message})


def profile_settings(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    else:
        return render(request, 'chat_room/profile_settings.html')
