from django.contrib import admin
from .models import *

admin.site.register(PhysicsTopic)
admin.site.register(Exam)
admin.site.register(ExamQuestion)
admin.site.register(ExamAttempt)
admin.site.register(QuestionResult)
admin.site.register(HintUsage)
