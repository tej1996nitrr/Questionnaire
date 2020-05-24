from rest_framework import serializers
from questions.models import Answer, Question 

class AnswerSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only= True)
    created_at = serializers.SerializerMethodField(read_only=True)
    likes_count = serializers.SerializerMethodField()
    user_has_voted = serializers.SerializerMethodField()
    class Meta:
        model = Answer
        exclude = ["question", "voters", "updated_at"]
        
    def get_created_at(self, instance):
        return instance.created_at.strftime("%B %d %Y")

    def get_likes_count(self, instance):
        return instance.voters.count()

    def get_user_has_voted(self, instance):
        request = self.context.get("request")
        return instance.voters.filter(pk=request.user.pk).exists()

class QuestionSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only= True)
    created_at = serializers.SerializerMethodField(read_only=True)
    slug = serializers.SlugField(read_only=True)
    answers_count = serializers.SerializerMethodField()
    user_has_answered = serializers.SerializerMethodField()

    class Meta:
        model = Question
        exclude = ["updated_at"]

    def get_created_at(self, instance):
        return instance.created_at.strftime("%B %d %Y")

    def get_answers_count(self,instance):
        print(instance)
        return instance.answers.count()

    def get_user_has_answered(self,instance):
        request = self.context.get("request")
        return instance.answers.filter(author=request.user).exists() 



    

