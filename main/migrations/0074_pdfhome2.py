# Generated by Django 5.1.2 on 2024-10-30 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0073_pdfhome'),
    ]

    operations = [
        migrations.CreateModel(
            name='PdfHome2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism_famlya', models.CharField(max_length=300)),
                ('rasm', models.ImageField(upload_to='media/')),
                ('manzil', models.CharField(max_length=300)),
                ('ikonka1', models.ImageField(upload_to='media/')),
                ('nomi1', models.ImageField(max_length=300, upload_to='')),
                ('nomi2', models.CharField(max_length=399)),
                ('tell_raqami', models.IntegerField()),
                ('nomi3', models.CharField(max_length=400)),
                ('email_nomi', models.CharField(max_length=400)),
                ('nomi4', models.CharField(max_length=500)),
                ('website_nomi', models.CharField(max_length=500)),
                ('nomi5', models.CharField(max_length=400)),
                ('instagarm_nomi', models.CharField(max_length=500)),
                ('ikonka_nomi2', models.CharField(max_length=600)),
                ('ikonka_nomi3', models.CharField(max_length=600)),
            ],
        ),
    ]