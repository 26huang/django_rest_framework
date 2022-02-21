# Run in Django shell
from api.models import Article
from api.serializers import ArticleSerializer, ArticleModelSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

# Insert data
a = Article(title='Test 1', author='Wei', email='wei@demo.com')
a.save()
# serialize an object
serializer = ArticleSerializer(a)
print(serializer.data)
# return object in JSON format
content = JSONRenderer().render(serializer.data)
print(content)
# return all article data objects
serializer = ArticleSerializer(Article.objects.all(), many=True)
print(serializer.data)
# show Serializer and ModelSerializer are the same. except ModelSerializers code are cleaner
print(ArticleModelSerializer())
print(ArticleSerializer())

# use postman to exercise GET, POST, and PUT
# GET localhost:8000/api/article/
# GET localhost:8000/api/detail/3
# POST localhost:8000/api/article/
# Body > Raw > {
#     "id": 3,
#     "title": "Test 3",
#     "author": "Wei3"
# }

