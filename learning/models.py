from django.db import models
from django.contrib.auth.models import User

class PhysicsTopic(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Exam(models.Model):
    title = models.CharField(max_length=200)
    duration = models.IntegerField(help_text="Minutes")

    def __str__(self):
        return self.title


class ExamQuestion(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    topic = models.ForeignKey(PhysicsTopic, on_delete=models.SET_NULL, null=True)

    question = models.TextField()
    option_a = models.CharField(max_length=200)
    option_b = models.CharField(max_length=200)
    option_c = models.CharField(max_length=200)
    option_d = models.CharField(max_length=200)

    correct_answer = models.CharField(max_length=1)

    # AI Hints
    hint_concept = models.TextField()
    hint_formula = models.TextField()
    hint_approach = models.TextField()


class ExamAttempt(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    submitted = models.BooleanField(default=False)
    violations = models.IntegerField(default=0)


class QuestionResult(models.Model):
    attempt = models.ForeignKey(ExamAttempt, on_delete=models.CASCADE)
    question = models.ForeignKey(ExamQuestion, on_delete=models.CASCADE)
    correct = models.BooleanField()


class HintUsage(models.Model):
    attempt = models.ForeignKey(ExamAttempt, on_delete=models.CASCADE)
    question = models.ForeignKey(ExamQuestion, on_delete=models.CASCADE)
    level = models.IntegerField()
    used_at = models.DateTimeField(auto_now_add=True)
