from django.views.generic.edit import FormView
from grading.forms import GradingForm
from grading.models import Grade, Candidate
from django.http import JsonResponse, HttpResponse
from django.views import View


class GradingView(FormView):
    template_name = 'grade_task.html'
    form_class = GradingForm
    success_url = '/grades-list/'

    def form_valid(self, form):
        recruiter = form.cleaned_data['recruiter']
        candidate = form.cleaned_data['candidate']
        task = form.cleaned_data['task']
        grade = form.cleaned_data['grade']

        if len(Grade.objects.filter(task=task, candidate=candidate)) is not 0:
            return HttpResponse('This task has already been graded!')

        else:
            Grade.objects.create(recruiter=recruiter, candidate=candidate, task=task, value=grade)

        return super(GradingView, self).form_valid(form)


class ListView(View):
    def get(self, request):
        candidates = Candidate.objects.all()
        grades = Grade.objects.all()
        json_data = []

        for candidate in candidates:
            candidate_grades = grades.filter(candidate_id=candidate.id).values('value')
            candidate_grades_list = []

            for grade in candidate_grades:
                candidate_grades_list.append(grade.get('value'))

            grade_sum = 0
            grade_amt = 0
            for grade in candidate_grades_list:
                grade_sum += grade
                grade_amt += 1

            if grade_amt > 0:
                avg_grade = grade_sum / grade_amt
            else:
                avg_grade = 0

            json_data.append(
                {
                    'pk': candidate.pk,
                    'full_name': candidate.first_name + ' ' + candidate.last_name,
                    'avg_grade': avg_grade,
                    'grades': candidate_grades_list
                }
            )

        response = JsonResponse(
            {'data': json_data}
        )

        return response
