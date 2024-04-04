import json

from django.http import HttpResponse

from .models import QuestDescription, QuestLongDescription, Quest, Question


# Create your views here.


def JsonResponse(obj):
    return HttpResponse(
        json.dumps(obj, ensure_ascii=False),
        content_type="application/json")


def ListDict(obj):
    return list(map(dict, obj))


def ListJsonResponse(obj):
    return JsonResponse(ListDict(obj))


def index(request):
    return HttpResponse("Hello World")


def get_quest_description(request):
    return ListJsonResponse(QuestDescription.objects.all())


def get_quest_long_description_by_id(request, pk):
    return JsonResponse(dict(QuestLongDescription.objects.filter(pk=pk)[0]))


def get_quest(request, pk):
    quest = dict(Quest.objects.filter(pk=pk)[0])
    quest["questions"] = ListDict(Question.objects.filter(quest=pk).order_by("order"))
    return JsonResponse(quest)
