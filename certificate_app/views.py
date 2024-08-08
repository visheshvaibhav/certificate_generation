from django.shortcuts import render, get_object_or_404, redirect
import random
import string
from .models import Certificate
from .forms import CertificateForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('generate_certificate')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


def generate_unique_certificate_id():
    characters = string.ascii_letters + string.digits
    while True:
        certificate_id = ''.join(random.choice(characters) for _ in range(8))
        if not Certificate.objects.filter(certificate_id=certificate_id).exists():
            return certificate_id


@login_required
def generate_certificate(request):
    if request.method == 'POST':
        form = CertificateForm(request.POST)
        if form.is_valid():
            certificate = form.save(commit=False)
            certificate.certificate_id = generate_unique_certificate_id()
            certificate.issue_date = form.cleaned_data['issue_date']
            certificate.save()
            return redirect('certificate_generated', certificate_id=certificate.certificate_id)
    else:
        form = CertificateForm()
    return render(request, 'generate_certificate.html', {'form': form})


def certificate_generated(request, certificate_id):
    certificate = get_object_or_404(Certificate, certificate_id=certificate_id)
    return render(request, 'certificate_template.html', {'certificate': certificate})


def certificate_details(request, certificate_id):
    certificate = get_object_or_404(Certificate, certificate_id=certificate_id)
    return render(request, 'certificate_details.html', {'certificate': certificate})


def verify_certificate(request):
    if request.method == 'POST':
        certificate_id = request.POST['certificate_id']
        certificate = get_object_or_404(
            Certificate, certificate_id=certificate_id)
        return redirect('certificate_details', certificate_id=certificate_id)
    return render(request, 'verify_certificate.html')


'''
# certificate_app/views.py
from django.shortcuts import render
import random
import string
from .models import Certificate
from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.decorators import permission_required


def generate_certificate(request):
    if request.method == 'POST':
        recipient_name = request.POST.get('recipient_name')  # Use .get() to avoid None if the field is empty
        if recipient_name:
            certificate_id = generate_unique_certificate_id()

            # Save the certificate to the database
            certificate = Certificate.objects.create(
                recipient_name=recipient_name,
                certificate_id=certificate_id,
            )
            certificate.save()

            # Pass the data to the template context
            return render(request, 'certificate_template.html', {'certificate': certificate})

    return render(request, 'generate_certificate.html')


def certificate_generated(request, certificate_id):
    certificate = get_object_or_404(Certificate, certificate_id=certificate_id)
    return render(request, 'certificate_template.html', {'certificate': certificate})

def generate_unique_certificate_id():
    characters = string.ascii_letters + string.digits
    while True:
        certificate_id = ''.join(random.choice(characters) for _ in range(8))
        if not Certificate.objects.filter(certificate_id=certificate_id).exists():
            return certificate_id

def certificate_details(request, certificate_id):
    certificate = get_object_or_404(Certificate, certificate_id=certificate_id)
    return render(request, 'certificate_template.html', {'certificate': certificate})

def verify_certificate(request):
    if request.method == 'POST':
        certificate_id = request.POST['certificate_id']
        certificate = get_object_or_404(Certificate, certificate_id=certificate_id)
        return redirect('certificate_details', certificate_id=certificate_id)

    return render(request, 'verify_certificate.html')
    '''
