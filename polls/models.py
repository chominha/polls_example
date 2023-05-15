from django.db import models
#오알엠을 사용하는 것이다.
# Create your models here.
class Question(models.Model): #레코드 하나를 객체로 가짐.
    question_text = models.CharField(max_length=200) #퀘스천 클래스임
    pub_date = models.DateField('date published') #퀘스천 클래스임.
    #질문. 날짜.
#인스턴스 : 클래스(추상화된 것 )의 객체(복제 판들)
#사는곳은? 하나가 퀘스천 클래스의 객체 하나임.

    def __str__(self):
        return self.question_text
    #스트링 메소드 객체를 print해서 정보를 알려줌.
    #특수 메소드
    #보여주고 싶은 객체를 출력해주는 메소드.
    #모델 = 테이블을 만드는 것.



class Choice(models.Model):#세가지 속성 값을 정의했다.
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
#서울. 투표수. 질문
    #ForeignKey(외래키 : 데이터 베이스. 다른 테이블의 기본키만 외래키가 될 수 있다.)
    def __str__(self):
        return self.choice_text



    #관리자 페이지를 이용하지만. 없다면 코드로 다 작성해야 했다.