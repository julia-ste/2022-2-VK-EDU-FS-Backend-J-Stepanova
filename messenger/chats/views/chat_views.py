from django.contrib.auth import get_user_model
from django.forms import model_to_dict
from django.http import JsonResponse, Http404
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_http_methods

from chats.models import Chat, ChatMember, Category
from utils.get_request_params import get_params


@require_http_methods(["GET"])
def chat_list(request, user_pk):
    user = get_object_or_404(get_user_model(), pk=user_pk)
    chats = user.user_chats.values("id", "title")

    return JsonResponse(
        list(chats),
        safe=False,
        json_dumps_params={"ensure_ascii": False},
        status=200
    )


@require_http_methods(["POST"])
def chat_create(request):
    user_pk = request.POST.get("user")
    user = get_object_or_404(get_user_model(), pk=user_pk)

    category_pk = request.POST.get("category")
    category = get_object_or_404(Category, pk=category_pk) if category_pk else None

    chat_params = get_params(request.POST, excluded=["user", "category"])
    chat = Chat.objects.create(author=user, category=category, **chat_params)
    chat.save()

    chat_member = ChatMember.objects.create(chat=chat, user=user)
    chat_member.save()

    return JsonResponse(
        model_to_dict(chat),
        json_dumps_params={"ensure_ascii": False},
        status=201
    )


@require_http_methods(["PATCH", "POST"])
def chat_update(request, pk):
    chat = get_object_or_404(Chat, pk=pk)

    category_pk = request.POST.get("category")
    category = get_object_or_404(Category, pk=category_pk) if category_pk else None

    chat_params = get_params(request.POST, excluded=["user", "category"])
    chat_params["category"] = category
    for key, value in chat_params.items():
        setattr(chat, key, value)

    chat.save()

    return JsonResponse(
        model_to_dict(chat),
        json_dumps_params={"ensure_ascii": False},
        status=200
    )


@require_http_methods(["GET"])
def chat_detail(request, pk):
    chat = get_object_or_404(Chat, pk=pk)

    return JsonResponse(
        model_to_dict(chat),
        json_dumps_params={"ensure_ascii": False},
        status=200
    )


@require_http_methods(["DELETE", "POST"])
def chat_delete(request, pk):
    chat = get_object_or_404(Chat, pk=pk)
    chat.delete()

    return JsonResponse(
        model_to_dict(chat),
        json_dumps_params={"ensure_ascii": False},
        status=200
    )


@require_http_methods(["POST"])
def chat_add_member(request, chat_pk):
    user_pk = request.POST.get("user")
    user = get_object_or_404(get_user_model(), id=user_pk)

    chat = get_object_or_404(Chat, pk=chat_pk)

    chat_member = ChatMember.objects.filter(chat=chat, user=user).first()
    if chat_member:
        raise Http404(f"User {user} already in chat {chat}!")

    chat_member = ChatMember.objects.create(chat=chat, user=user)
    chat_member.save()

    return JsonResponse(
        {"user": str(user), "chat": str(chat)},
        json_dumps_params={"ensure_ascii": False},
        status=200
    )


@require_http_methods(["DELETE", "POST"])
def chat_delete_member(request, chat_pk):
    user_pk = request.POST.get("user")
    user = get_object_or_404(get_user_model(), id=user_pk)

    chat = get_object_or_404(Chat, pk=chat_pk)

    chat_member = ChatMember.objects.filter(chat=chat, user=user).first()
    if not chat_member:
        raise Http404(f"User {user} is not a member of chat {chat}!")

    chat_member.delete()

    return JsonResponse(
        {"user": str(user), "chat": str(chat)},
        json_dumps_params={"ensure_ascii": False},
        status=200
    )
