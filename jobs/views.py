from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

from .models import Job
from .serializers import JobSerializer
from rest_framework.permissions import IsAuthenticated
from accounts.permissions import IsEmployer

class JobListCreateView(generics.ListCreateAPIView):
    queryset = Job.objects.all().order_by("-created_at")
    serializer_class = JobSerializer

    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
    ]

    filterset_fields = [
        "location",
        "job_type",
        "company",
    ]

    search_fields = [
        "title",
        "company",
        "location",
        "description",
        "requirements",
    ]

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsEmployer()]

        return [IsAuthenticated()]

    def perform_create(self, serializer):
        serializer.save(employer=self.request.user)


class JobDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

    def get_permissions(self):
        if self.request.method in ["PUT", "PATCH", "DELETE"]:
            return [IsEmployer()]

        return [IsAuthenticated()]

    def perform_update(self, serializer):
        if serializer.instance.employer != self.request.user:
            from rest_framework.exceptions import PermissionDenied

            raise PermissionDenied(
                "You can only modify your own job postings."
            )

        serializer.save()

    def perform_destroy(self, instance):
        if instance.employer != self.request.user:
            from rest_framework.exceptions import PermissionDenied

            raise PermissionDenied(
                "You can only delete your own job postings."
            )

        instance.delete()