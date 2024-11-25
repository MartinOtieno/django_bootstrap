# Generated by Django 4.2 on 2024-11-25 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_booking_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadedImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=108)),
                ('image', models.ImageField(upload_to='uploaded_images/')),
            ],
        ),
    ]