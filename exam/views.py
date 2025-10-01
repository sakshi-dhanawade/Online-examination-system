from django.shortcuts import render, get_object_or_404
from .models import Exam
from django.utils import timezone
from .models import Exam, Question, Choice, Attempt
from django.contrib.auth.decorators import login_required

def welcome(request):
    return render(request, 'exam/welcome.html')



def exam_list(request):
    exams = Exam.objects.all()
    return render(request, 'exam/exam_list.html', {'exams': exams})


def exam_detail(request, pk):
    exam = get_object_or_404(Exam, pk=pk)
    questions = exam.questions.all()
    return render(request, 'exam/exam_detail.html', {
        'exam': exam,
        'questions': questions
    })


@login_required
def take_exam(request, pk):
    exam = get_object_or_404(Exam, pk=pk)
    questions = exam.questions.prefetch_related('choices').all()

    if request.method == 'POST':
        # Create a new attempt for this student
        attempt = Attempt.objects.create(student=request.user, exam=exam, started_at=timezone.now())
        score = 0

        # Check each question
        for q in questions:
            selected_id = request.POST.get(f"question_{q.id}")
            if selected_id:
                choice = Choice.objects.get(pk=selected_id)
                if choice.is_correct:
                    score += q.marks

        attempt.score = score
        attempt.finished_at = timezone.now()
        attempt.save()

        return render(request, 'exam/result.html', {
            'exam': exam,
            'score': score,
            'total': sum(q.marks for q in questions)
        })

    return render(request, 'exam/take_exam.html', {
        'exam': exam,
        'questions': questions
    })

def logout_message(request):
    return render(request, 'exam/logout_message.html')
