# Generated by Django 5.1.2 on 2024-10-31 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0074_pdfhome2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pdfhome2',
            name='nomi1',
            field=models.CharField(max_length=300),
        ),
    ]