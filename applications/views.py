from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from jobs.models import Job
from .models import Application
from .serializers import ApplicationSerializer
from accounts.permissions import IsCandidate, IsEmployer



class ApplyToJobView(generics.CreateAPIView):
    serializer_class = ApplicationSerializer
    permission_classes = [IsCandidate]

    def create(self, request, *args, **kwargs):
        job = get_object_or_404(
            Job,
            pk=kwargs["job_id"]
        )

        if Application.objects.filter(
            job=job,
            candidate=request.user
        ).exists():
            raise ValidationError(
                "You have already applied for this job."
            )

        application = Application.objects.create(
            job=job,
            candidate=request.user
        )

        serializer = self.get_serializer(application)

        return Response(
            serializer.data,
            status=201
        )


class MyApplicationsView(generics.ListAPIView):
    serializer_class = ApplicationSerializer
    permission_classes = [IsCandidate]

    def get_queryset(self):
        return Application.objects.filter(
            candidate=self.request.user
        )

class JobApplicationsView(generics.ListAPIView):
    serializer_class = ApplicationSerializer
    permission_classes = [IsEmployer]

    def get_queryset(self):
        return Application.objects.filter(
            job__employer=self.request.user
        )