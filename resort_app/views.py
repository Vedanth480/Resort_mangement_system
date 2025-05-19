from django.core.mail import send_mail
from django.http import HttpResponse
from django.conf import settings

def send_notification_email(to_email, subject, message):
    send_mail(
        subject,
        message,
        settings.EMAIL_HOST_USER,  # Correct: Uses the Gmail sender defined in settings.py
        [to_email],
        fail_silently=False,       # Good: Raises error if sending fails
    )

def test_email(request):
    # Sample test email content
    subject = "Test Email from Django"
    message = "This is a test message to check email functionality."
    to_email = "negga0045@gmail.com"  # ✅ Replace with any test email

    send_notification_email(to_email, subject, message)
    return HttpResponse("Email has been sent successfully.")
