from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Job, Applicant
from .forms import ApplicantForm, JobForm

# ---------- PUBLIC VIEWS ----------

def job_list(request):
    role = request.GET.get('role', '')        # Filter by job role
    jobs = Job.objects.filter(title__icontains=role) if role else Job.objects.all()
    return render(request, 'jobs/job_list.html', {'jobs': jobs, 'role': role})

def apply_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    if request.method == 'POST':
        form = ApplicantForm(request.POST)
        if form.is_valid():
            applicant = form.save(commit=False)
            applicant.job = job
            try:
                applicant.save()
                messages.success(request, 'Application submitted successfully!')
                return redirect('job_list')
            except Exception:
                messages.error(request, 'You already applied for this job!')
        else:
            messages.error(request, 'Please fill the form correctly.')
    else:
        form = ApplicantForm()
    return render(request, 'jobs/apply.html', {'form': form, 'job': job})

# ---------- ADMIN VIEWS ----------

def admin_dashboard(request):
    role = request.GET.get('role', '')
    jobs = Job.objects.filter(title__icontains=role) if role else Job.objects.all()
    applicants = Applicant.objects.select_related('job').all()
    return render(request, 'jobs/admin_dashboard.html', {
        'jobs': jobs, 'applicants': applicants, 'role': role
    })

def add_job(request):
    form = JobForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Job added!')
        return redirect('admin_dashboard')
    return render(request, 'jobs/job_form.html', {'form': form, 'action': 'Add'})

def edit_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    form = JobForm(request.POST or None, instance=job)
    if form.is_valid():
        form.save()
        messages.success(request, 'Job updated!')
        return redirect('admin_dashboard')
    return render(request, 'jobs/job_form.html', {'form': form, 'action': 'Edit'})

def delete_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    job.delete()
    messages.success(request, 'Job deleted!')
    return redirect('admin_dashboard')