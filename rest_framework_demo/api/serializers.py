from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.Serializer):
    """
    Functional based api using Serializer only.
    """
    title = serializers.CharField(max_length=100)
    author = serializers.CharField(max_length=100)
    email = serializers.EmailField(max_length=100)
    date = serializers.DateTimeField()

    def create(self, validated_data):
        return Article.objects.create(validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.author = validated_data.get('author', instance.author)
        instance.email = validated_data.get('email', instance.email)
        instance.date = validated_data.get('date', instance.date)
        instance.save()
        return instance


class ArticleModelSerializer(serializers.ModelSerializer):
    """
    API using ModelSerializer. This is preferred over regular Serializer due to simplicity.
    """
    class Meta:
        model = Article
        fields = '__all__' # Use this to get all fields.
        # fields = ['id', 'title', 'author', 'date', 'email',]
