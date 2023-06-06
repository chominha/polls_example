from django.contrib import admin
from polls.models import Question, Choice
# Register your models here.

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2
    #StackedInline 쌓는 형식
    #TabularInline

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [('Question Statement', {'fields' : ['question_text']}),
                 ('Date Information', {'fields': ['pub_date'], 'classes' : ['collapse']})]
    inlines = [ChoiceInline]
    list_display =('question_text', 'pub_date')
    list_filter = ['pub_date'] #장고는 필터를 자동으로 구성해준다.
    search_fields = ['question_text'] #LIKE쿼리 사용.

#필드셋은 리스트로 되어있다. 리스트 안에 튜플로 들어가있다.
#딕셔너리안에 추가하면 추가되는거야.
#리스트디스플레이스는 튜플로


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)

#ui를 변경하는거지 데이터 베이스를 변경하는 것이 아니다.