from django.db import models

class Payment(models.Model):
    order_id = models.CharField(max_length=100)  # Assuming you have an external order ID you wish to track
    razorpay_payment_id = models.CharField(max_length=255, unique=True)  # Razorpay's payment ID
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Amount paid
    is_successful = models.BooleanField(default=False)  # Payment status
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp of the payment

    def __str__(self):
        return f"Payment {self.razorpay_payment_id} - {'Successful' if self.is_successful else 'Failed'}"
