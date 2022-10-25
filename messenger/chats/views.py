from django.http import JsonResponse, Http404
from django.views.decorators.http import require_GET, require_POST

chats = [
    {'id': 1, 'title': 'Chat 1'},
    {'id': 2, 'title': 'Chat 2'},
    {'id': 3, 'title': 'Chat 3'},
    {'id': 4, 'title': 'Chat 4'},
]


@require_GET
def chat_list(request):
    return JsonResponse({'chats': chats})


@require_GET
def chat_detail(request, pk):
    if pk < 1 or len(chats) < pk:
        raise Http404(f'Chat with id={pk} does not exist!')
    return JsonResponse(chats[pk - 1])


@require_POST
def chat_create(request):
    title = request.POST.get('title')
    next_id = len(chats) + 1
    new_chat = {'id': next_id, 'title': title}
    chats.append(new_chat)
    return JsonResponse(new_chat)
