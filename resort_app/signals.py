from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import BookingManagement

@receiver(post_save, sender=BookingManagement)
def send_booking_confirmation_email(sender, instance, created, **kwargs):
    if created:  # Send only on new bookings
        subject = f"Booking Confirmation - Booking #{instance.id}"

        message = f"""Dear {instance.customer.name},

Your booking for room {instance.room.room_number} has been confirmed.

Booking Details:
Check-in Date: {instance.check_in_date}
Check-out Date: {instance.check_out_date}
Number of Guests: {instance.number_of_guests}
Total Amount: ₹{instance.total_amount}

We look forward to hosting you!
In case any cancellation,no refund will be provided.
Best regards,
Your Resort Team
"""

        try:
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                [instance.customer.email],
                fail_silently=False,
            )
            print(f"Booking confirmation email sent to {instance.customer.email}")
        except Exception as e:
            print(f"Email sending failed: {e}")
