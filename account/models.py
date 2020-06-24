from django.db import models
from django.conf import settings
from django.templatetags.static import static
from django.forms import ValidationError


class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    email = models.CharField(max_length=100, blank=True, unique=True)

    phone = models.CharField(max_length=20, blank=True)
    room_number = models.CharField(max_length=20, blank=True)

    image = models.ImageField(upload_to='user-profile-images', blank=True)

    is_active = models.BooleanField(default=True)

    subjects = models.ManyToManyField('account.Subject', related_name='teacher_subjects', blank=True)

    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'

    def __str__(self):
        name = self.email

        if self.first_name or self.last_name:
            name = f'{self.first_name} {self.last_name}'.strip()

        return name

    def get_profile_image(self):
        if self.image:
            if settings.DEBUG:
                return '{}{}'.format(settings.MEDIA_ROOT, self.image.url)

            return self.image.url

        return static('images/default-avatar.jpg')

    def get_subjects(self):
        return [subject.subject for subject in self.subjects.filter(is_active=True).order_by('subject')]


class Subject(models.Model):
    subject = models.CharField(max_length=100)

    is_active = models.BooleanField(default=True)

    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)

    def __str__(self):
        return self.subject
