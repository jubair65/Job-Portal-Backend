from django.urls import path

from .views import (
    ApplyToJobView,
    MyApplicationsView,
    JobApplicationsView,
    ApplicationStatusUpdateView,
)


urlpatterns = [
    path("jobs/<int:job_id>/apply/", ApplyToJobView.as_view(), name="apply-to-job"),
    path("my-applications/", MyApplicationsView.as_view(), name="my-applications"),
    path("job-applications/", JobApplicationsView.as_view(), name="job-applications"),
    path("<int:pk>/status/", ApplicationStatusUpdateView.as_view(), name="application-status-update"),
]