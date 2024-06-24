from django.db import models

class Candlestick(models.Model):

    TIME_FRAME_CHOICES = [
        ('W', 'Weekly'),
        ('D1', 'Daily'),
        ('H4', '4-Hour')
    ]

    id = models.AutoField(primary_key=True)
    date = models.DateTimeField()
    open_price = models.DecimalField(max_digits=10, decimal_places=2)
    high_price = models.DecimalField(max_digits=10, decimal_places=2)
    low_price = models.DecimalField(max_digits=10, decimal_places=2)
    close_price = models.DecimalField(max_digits=10, decimal_places=2)
    time_frame = models.CharField(max_length=2, choices=TIME_FRAME_CHOICES)

    def __str__(self):
        return f"Candlestick on {self.date} ({self.get_time_frame_display()})"
