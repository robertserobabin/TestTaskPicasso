# Generated by Django 4.2.7 on 2023-11-01 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.FileField(upload_to='uploaded_files/', verbose_name='файл'),
        ),
    ]