# Generated by Django 5.1.2 on 2024-11-01 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0086_pdfpast'),
    ]

    operations = [
        migrations.AddField(
            model_name='project_kard',
            name='href',
            field=models.CharField(default=1, max_length=300),
            preserve_default=False,
        ),
    ]