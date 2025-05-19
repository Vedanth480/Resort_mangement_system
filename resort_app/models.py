from django.db import models

# Room Types Choices
ROOM_TYPES = [
    ('Single', 'Single'),
    ('Double', 'Double'),
    ('Suite', 'Suite'),
]

# Booking Status Choices
BOOKING_STATUSES = [
    ('Pending', 'Pending'),
    ('Confirmed', 'Confirmed'),
    ('Cancelled', 'Cancelled'),
]

# 1. Customer Details
class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    id_proof = models.CharField(max_length=100, blank=True, null=True)  # optional

    def __str__(self):
        return self.name

# 2. Room Management
class RoomManagement(models.Model):
    room_number = models.CharField(max_length=10, unique=True)
    room_type = models.CharField(max_length=50, choices=ROOM_TYPES)
    capacity = models.PositiveIntegerField()
    price_per_night = models.DecimalField(max_digits=8, decimal_places=2)
    is_available = models.BooleanField(default=True)
    description = models.TextField()
    image_url = models.URLField(blank=True, null=True)  # optional

    def __str__(self):
        return f"Room {self.room_number} ({self.room_type})"

# 3. Booking Management
class BookingManagement(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='bookings')
    room = models.ForeignKey(RoomManagement, on_delete=models.CASCADE, related_name='bookings')
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    number_of_guests = models.PositiveIntegerField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    booking_status = models.CharField(max_length=20, choices=BOOKING_STATUSES, default="Pending")
    booking_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking #{self.id} - {self.customer.name}"

# 4. Room Services
class RoomService(models.Model):
    room = models.ForeignKey(RoomManagement, on_delete=models.CASCADE, related_name='services')
    service_type = models.CharField(max_length=50)  # Cleaning, Laundry, etc.
    request_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default="Pending")  # Pending, Completed

    def __str__(self):
        return f"{self.service_type} for Room {self.room.room_number}"
