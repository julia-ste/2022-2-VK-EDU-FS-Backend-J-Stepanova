from django.contrib.auth import get_user_model
from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_http_methods

from chats.models import Chat, Message
from utils.get_request_params import get_params


@require_http_methods(["GET"])
def message_list(request, chat_pk):
    chat = get_object_or_404(Chat, pk=chat_pk)
    messages = chat.chat_messages.values("id", "text")

    return JsonResponse(
        list(messages),
        safe=False,
        json_dumps_params={"ensure_ascii": False},
        status=200
    )


@require_http_methods(["POST"])
def message_create(request, chat_pk):
    chat = get_object_or_404(Chat, pk=chat_pk)

    user_pk = request.POST.get("user")
    user = get_object_or_404(get_user_model(), id=user_pk)

    message_params = get_params(request.POST, excluded=["user"])
    message = Message.objects.create(chat=chat, author=user, **message_params)
    message.save()

    return JsonResponse(
        model_to_dict(message),
        json_dumps_params={"ensure_ascii": False},
        status=201
    )


@require_http_methods(["PATCH", "POST"])
def message_update(request, pk):
    message = get_object_or_404(Message, pk=pk)

    message_params = get_params(request.POST, excluded=["user"])
    for key, value in message_params.items():
        setattr(message, key, value)

    message.save()

    return JsonResponse(
        model_to_dict(message),
        json_dumps_params={"ensure_ascii": False},
        status=200
    )


@require_http_methods(["GET"])
def message_detail(request, pk):
    message = get_object_or_404(Message, pk=pk)

    return JsonResponse(
        model_to_dict(message),
        json_dumps_params={"ensure_ascii": False},
        status=200
    )


@require_http_methods(["DELETE", "POST"])
def message_delete(request, pk):
    message = get_object_or_404(Message, pk=pk)
    message.delete()

    return JsonResponse(
        model_to_dict(message),
        json_dumps_params={"ensure_ascii": False},
        status=200
    )


@require_http_methods(["PATCH", "POST"])
def message_delete(request, pk):
    message = get_object_or_404(Message, pk=pk)
    message.is_read = True
    message.save()

    return JsonResponse(
        model_to_dict(message),
        json_dumps_params={"ensure_ascii": False},
        status=200
    )
