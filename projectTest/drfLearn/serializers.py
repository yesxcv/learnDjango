from rest_framework import serializers
from drfLearn.models import Article
from django.contrib.auth import  get_user_model

User = get_user_model()

# class ArticleSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=True,allow_blank=True,max_length=100)
#     body = serializers.CharField(required=False,allow_blank=True)
#     author = serializers.ReadOnlyField(source="author.id")
#     status = serializers.ChoiceField(choices=Article.STATUS_CHOICES, default='p')
#     create_date = serializers.DateTimeField(read_only=True)
#
#     def create(self, validated_data):
#         return Article.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get("title",instance.title)
#         instance.body = validated_data.get("body",instance.body)
#         instance.save()
#         return  instance


class UserSerializer(serializers.ModelSerializer):
    # articles = serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    # articles = serializers.StringRelatedField(many=True,read_only=True)
    articles = serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='article-detail', lookup_field='pk')
    class Meta:
        model = User
        fields = ["id","username","email","articles"]
        read_only_fields = ["id","username"]

class ArticleSerializer(serializers.ModelSerializer):
    # author = UserSerializer()
    full_status = serializers.ReadOnlyField(source="get_status_display")
    cn_status = serializers.SerializerMethodField()
    create_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S",required=False,read_only=True)
    class Meta:
        model = Article
        fields = "__all__"
        read_only_fields = ("id","author","create_date")
        depth = 1

    def to_representation(self, value):
        data = super().to_representation(value)
        data["total_likes"] = value.like_by.count()
        return  data

    def get_cn_status(self,obj):
        if obj.status == 's':
            return "错了"
        if obj.status == "p":
            return "已发表"
        if obj.status == "d":
            return "草稿"
        else:
            return "未知"