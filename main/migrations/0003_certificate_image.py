# Generated by Django 3.2.19 on 2024-05-13 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20240509_1001'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificate',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='certificateS'),
        ),
    ]
