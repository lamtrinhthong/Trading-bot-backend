# Generated by Django 5.0.6 on 2024-06-22 19:40

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Candlestick",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("date", models.DateTimeField()),
                ("open_price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("high_price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("low_price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("close_price", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "time_frame",
                    models.CharField(
                        choices=[("W", "Weekly"), ("D1", "Daily"), ("H4", "4-Hour")],
                        max_length=2,
                    ),
                ),
            ],
        ),
    ]
