import io
import pandas as pd

from django.shortcuts import redirect
from django.views.generic import TemplateView, DetailView, FormView

from account.models import Teacher, Subject
from account.forms import ImportForm


class HomeView(TemplateView):
    template_name = "account/home.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        teachers = Teacher.objects.filter(is_active=True).order_by('last_name')
        filtered_letters = self.get_filtered_letters(teachers)

        filter_by_subject = self.request.GET.get('fs')
        filter_by_letter = self.request.GET.get('fl')

        if filter_by_subject:
            teachers = teachers.filter(subjects__id=filter_by_subject)

        if filter_by_letter:
            teachers = teachers.filter(last_name__istartswith=filter_by_letter[0])

        ctx['teachers'] = teachers
        ctx['subjects'] = Subject.objects.filter(is_active=True).order_by('subject')

        ctx['filtered_letters'] = filtered_letters

        ctx['filter_by_subject'] = int(filter_by_subject) if filter_by_subject else None
        ctx['filter_by_letter'] = filter_by_letter

        return ctx

    def get_filtered_letters(self, teachers):
        arr = []
        for teacher in teachers:
            if teacher.last_name[0] not in arr:
                arr.append(teacher.last_name[0])

        return arr


class TeacherDetailView(DetailView):
    template_name = "account/teacher_details.html"
    model = Teacher

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        ctx['teachers'] = Teacher.objects.filter(is_active=True)

        return ctx


class TeacherImportView(FormView):
    template_name = "account/teacher_import.html"
    form_class = ImportForm

    def form_valid(self, form):
        cd = form.cleaned_data

        data = cd['file'].read().decode('utf-8')
        stringIO = io.StringIO(data)
        df = pd.read_csv(stringIO)

        for record in df.values:
            first_name = record[0]
            last_name = record[1]
            image = record[2]
            email = record[3]
            phone = record[4]
            room = record[5]
            subjects = record[6]

            if email and type(email) == str:
                teacher, created = Teacher.objects.get_or_create(email=email)

                if created:
                    teacher.first_name = first_name
                    teacher.last_name = last_name
                    teacher.image = f'user-profile-images/{image}' if image else ''
                    teacher.phone = phone
                    teacher.room = room

                    teacher.save()

                    if subjects and type(subjects) == str:
                        for subject in subjects.split(',')[:5]:
                            subject = subject.strip()

                            try:
                                sobj = Subject.objects.get(subject__iexact=subject)
                            except Subject.DoesNotExist:
                                sobj = Subject.objects.create(subject=subject.title())

                            teacher.subjects.add(sobj)

        return redirect('account:home')
