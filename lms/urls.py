from django.contrib import admin
from django.urls import path, include
from exam import views as exam_views
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',exam_views.welcome, name='welcome'),
    path('courses/', RedirectView.as_view(pattern_name='welcome', permanent=False)),
    path('exams/', include('exam.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout-message/', exam_views.logout_message, name='logout_message'),
]

