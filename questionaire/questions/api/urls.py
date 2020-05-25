from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import QuestionViewset as qv
from .views import AnswerCreateAPIView,AnswerListAPIView, AnswerRUDAPIView

router = DefaultRouter()
router.register(r"", qv)

urlpatterns = [
    path("questions/", include(router.urls)),
    path("questions/<slug:slug>/answer/",AnswerCreateAPIView.as_view(), name="answer-create" ),
    path("questions/<slug:slug>/answers/",AnswerListAPIView.as_view(), name="answer-list" ),
    path("answers/<int:pk>",AnswerRUDAPIView.as_view(), name="answer-detail" ),


] 