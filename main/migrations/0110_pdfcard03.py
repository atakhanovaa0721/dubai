# Generated by Django 5.1.2 on 2024-11-03 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0109_pdfcard3'),
    ]

    operations = [
        migrations.CreateModel(
            name='PdfCard03',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi1', models.CharField(max_length=300)),
                ('nomi2', models.CharField(max_length=300)),
                ('rasm', models.ImageField(upload_to='media/')),
                ('text1', models.TextField()),
                ('text2', models.TextField()),
            ],
        ),
    ]
