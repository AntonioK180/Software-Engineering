from djangoProject.processors.api_processor import ApiProcessor

from django.http import HttpResponse, JsonResponse
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def longest_comment(request):
    return JsonResponse(ApiProcessor.longest_comment(), safe=False)

def post_with_longest_title(request):
    return JsonResponse(ApiProcessor.post_with_longest_title(), safe=False)