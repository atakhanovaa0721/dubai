# Generated by Django 5.0.3 on 2024-10-08 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0028_recent'),
    ]

    operations = [
        migrations.CreateModel(
            name='OY',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=200)),
                ('raqam', models.IntegerField()),
            ],
        ),
    ]
