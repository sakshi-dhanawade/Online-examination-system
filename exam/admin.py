from django.contrib import admin
from .models import Exam, Question, Choice, Attempt

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'exam', 'marks')
    inlines = [ChoiceInline]

class ExamAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'duration_minutes')

class AttemptAdmin(admin.ModelAdmin):
    list_display = ('student', 'exam', 'score', 'started_at')

admin.site.register(Exam, ExamAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Attempt, AttemptAdmin)


