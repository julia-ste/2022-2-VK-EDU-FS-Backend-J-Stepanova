from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_http_methods

from .models import Chat, Message, ChatMember


@require_http_methods(["GET"])
def chat_list(request, user_pk):
    chats = get_object_or_404(get_user_model(), id=user_pk).user_chats.values("id", "title")
    return JsonResponse(
        list(chats),
        safe=False,
        json_dumps_params={"ensure_ascii": False},
        status=200
    )


@require_http_methods(["GET"])
def message_list(request, chat_pk):
    messages = get_object_or_404(Chat, pk=chat_pk).chat_messages.values("id", "text")
    return JsonResponse(
        list(messages),
        safe=False,
        json_dumps_params={"ensure_ascii": False},
        status=200
    )


@require_http_methods(["POST"])
def chat_create(request):
    title = request.POST.get("title")
    author_pk = request.POST.get("author")

    author = get_object_or_404(get_user_model(), pk=author_pk)

    chat = Chat.objects.create(title=title, author=author)
    chat.save()

    chat_member = ChatMember.objects.create(chat=chat, user=author)
    chat_member.save()

    return JsonResponse(
        {'created chat': chat.title},
        safe=False,
        json_dumps_params={"ensure_ascii": False},
        status=201
    )


@require_http_methods(["POST"])
def message_create(request, chat_pk):
    chat = get_object_or_404(Chat, pk=chat_pk)

    text = request.POST.get("text")
    user_pk = request.POST.get("user")

    user = get_object_or_404(get_user_model(), id=user_pk)

    message = Message.objects.create(chat=chat, user=user, text=text)
    message.save()

    return JsonResponse(
        {'created message': message.text},
        safe=False,
        json_dumps_params={"ensure_ascii": False},
        status=201
    )


@require_http_methods(["PATCH", "POST"])
def chat_update(request, pk):
    chat = get_object_or_404(Chat, pk=pk)
    chat.title = request.POST.get("title")
    chat.save()

    return JsonResponse(
        {"updated chat title": chat.title},
        status=200
    )


@require_http_methods(["PATCH", "POST"])
def message_update(request, pk):
    message = get_object_or_404(Message, pk=pk)
    message.text = request.POST.get("text")
    message.save()

    return JsonResponse(
        {"updated message": message.text},
        safe=False,
        status=200
    )


@require_http_methods(["GET"])
def chat_detail(request, pk):
    chat = get_object_or_404(Chat, pk=pk)
    return JsonResponse(
        {'chat': chat.title},
        safe=False,
        json_dumps_params={"ensure_ascii": False},
        status=200
    )


@require_http_methods(["GET"])
def message_detail(request, pk):
    message = get_object_or_404(Message, pk=pk)
    return JsonResponse(
        {'message': message.text},
        safe=False,
        json_dumps_params={"ensure_ascii": False},
        status=200
    )


@require_http_methods(["DELETE", "POST"])
def chat_delete(request, pk):
    chat = get_object_or_404(Chat, pk=pk)
    chat.delete()
    return JsonResponse(
        {"deleted chat": chat.title},
        safe=False,
        status=200
    )


@require_http_methods(["DELETE", "POST"])
def message_delete(request, pk):
    message = get_object_or_404(Message, pk=pk)
    message.delete()
    return JsonResponse(
        {"deleted message": message.text},
        safe=False,
        status=200
    )
