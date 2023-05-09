
from django.contrib import admin
from django.urls import path, include
from polls import views

app_name = 'polls' #애플리케이션의 이름을 정의해줘야 한다.

urlpatterns = [

    path('', views.index, name='index'),#이미 프로젝트 urls에 정의되어 있어서 .. 이미 polls에 접속한 후의 일이기 떄문에 'polls/' 적을 필요 없어'
    path('polls/<int:question_id>/', views.detail, name='detail'),
    path('polls/<int:question_id>/vote/',views.vote, name='vote'),
    path('polls/int:<question_id>/results/', views.results, name='results'),
    #url과 뷰 함수와 연결

]