from django.contrib import admin

from .models import Question, Choice

admin.site.site_header = 'Russia admin'
admin.site.site_title = 'Russia polls'
admin.site.index_header = 'Russia polls, instigated by Putin, The Great'

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields' : ['question_text']}),
    ('Date Information', {'fields' : ['pub_date'], 'classes' : ['collapse']}),]
    inlines = [ChoiceInline]


# admin.site.register(Question)
# admin.site.register(Choice)
admin.site.register(Question, QuestionAdmin)


