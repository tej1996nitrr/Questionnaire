from rest_framework import viewsets
from questions.api.serializers import QuestionSerializer
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