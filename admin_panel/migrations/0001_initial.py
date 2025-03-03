# Generated by Django 5.1.6 on 2025-03-03 19:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_city', models.CharField(max_length=100)),
                ('to_city', models.CharField(max_length=100)),
                ('departure_time', models.DateTimeField()),
                ('arrival_time', models.DateTimeField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_seats', models.IntegerField()),
                ('available_seats', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seat_number', models.IntegerField()),
                ('purchase_date', models.DateTimeField(auto_now_add=True)),
                ('is_purchased', models.BooleanField(default=False)),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_panel.route')),
            ],
        ),
    ]
