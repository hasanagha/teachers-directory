# Third party imports
from django.urls import path
from django.contrib.auth.decorators import login_required

from account.views import *


app_name = 'account'

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("<int:pk>/", TeacherDetailView.as_view(), name="teacher-details"),
    path("import/", login_required(TeacherImportView.as_view()), name="teacher-import-form"),
]
