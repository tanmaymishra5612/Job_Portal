from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    skills = models.CharField(max_length=300)
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Applicant(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applicants')
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)   # Prevents duplicate applications
    phone = models.CharField(max_length=15)
    applied_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('job', 'email')   # One application per job per email

    def __str__(self):
        return f"{self.name} → {self.job.title}"