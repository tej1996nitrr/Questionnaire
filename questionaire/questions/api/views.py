from rest_framework import viewsets, generics
from rest_framework.exceptions import ValidationError
from questions.api.serializers import QuestionSerializer,AnswerSerializer
from questions.models import Question 
from rest_framework.permissions import IsAuthenticated
from questions.api.permissions import IsAuthorOrReadOnly


class QuestionViewset(viewsets.ModelViewSet):

    queryset = Question.objects.all()
    lookup_field = "slug"
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def perform_create(self, serializer): #to add author field automatically    
        serializer.save(author=self.request.user)

class AnswerViewset(generics.CreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]
   
    def perform_create(self, serializer): #to add author field automatically  
        request_user = self.request.user
        kwarg_slug = self.kwargs.get("slug")
        question = get_object_or_404(Answer, slug=k)
        if question.answers.filter(author=request_user).exists():
            raise ValidationError("You have already answered this question.") 
        serializer.save(author=self.request.user, question=question)