from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Count
from .models import *

@login_required
def start_exam(request, exam_id):
    exam = get_object_or_404(Exam, id=exam_id)
    questions = ExamQuestion.objects.filter(exam=exam)

    attempt, _ = ExamAttempt.objects.get_or_create(
        student=request.user,
        exam=exam
    )

    if request.method == "POST":
        score = 0
        for q in questions:
            selected = request.POST.get(str(q.id))
            correct = selected == q.correct_answer
            if correct:
                score += 1

            QuestionResult.objects.create(
                attempt=attempt,
                question=q,
                correct=correct
            )

        attempt.score = score
        attempt.submitted = True
        attempt.save()
        return redirect('analytics')

    return render(request, 'exam.html', {
        'exam': exam,
        'questions': questions,
        'duration': exam.duration * 60,
        'attempt': attempt
    })


@login_required
def get_hint(request, question_id, level):
    question = get_object_or_404(ExamQuestion, id=question_id)

    HintUsage.objects.create(
        attempt=ExamAttempt.objects.filter(
            student=request.user,
            exam=question.exam
        ).last(),
        question=question,
        level=level
    )

    hints = {
        1: question.hint_concept,
        2: question.hint_formula,
        3: question.hint_approach
    }

    return JsonResponse({"hint": hints[level]})


@login_required
def analytics(request):
    results = QuestionResult.objects.filter(
        attempt__student=request.user,
        correct=False
    ).values(
        'question__topic__name'
    ).annotate(
        total=Count('id')
    )

    return render(request, 'analytics.html', {'results': results})
