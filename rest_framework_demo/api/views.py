from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Article
from .serializers import ArticleModelSerializer
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
# add csrf_exempt to allow post to work. this is not recommended for security reasons.
@csrf_exempt
def article_list(request):
    """
    Endpoint to get all articles in the database
    :param request: build in object
    :type request: object
    :return: all articles
    :rtype: json
    """
    if request.method == 'GET':
        article = Article.objects.all()
        serializer = ArticleModelSerializer(article, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ArticleModelSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def article_detail(request, pk):
    """
    Endpoint to get article by pk
    :param request: build in object
    :type request: object
    :param pk: primary key of article
    :type pk: int
    :return: article data
    :rtype: json
    """
    try:
        article = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ArticleModelSerializer(article)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ArticleModelSerializer(article, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        article.delete()
        return HttpResponse(status=204)