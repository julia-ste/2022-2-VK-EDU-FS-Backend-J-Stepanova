from django.contrib.auth import get_user_model
from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET"])
def user_detail(request, pk):
    user = get_object_or_404(get_user_model(), pk=pk)

    return JsonResponse(
        model_to_dict(user),
        json_dumps_params={"ensure_ascii": False},
        status=200
    )
