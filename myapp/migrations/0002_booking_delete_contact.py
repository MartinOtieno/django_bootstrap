# Generated by Django 5.1.3 on 2024-11-13 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('people', models.PositiveIntegerField()),
                ('message', models.TextField(blank=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
    ]
