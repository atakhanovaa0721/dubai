# Generated by Django 5.1.2 on 2024-11-01 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0095_pdftxt8_text7_pdftxt8_text8_pdftxt8_text9'),
    ]

    operations = [
        migrations.CreateModel(
            name='PdfImg8',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='media/')),
                ('img2', models.ImageField(upload_to='media/')),
                ('img3', models.ImageField(upload_to='media/')),
                ('img4', models.ImageField(upload_to='media/')),
                ('img5', models.ImageField(upload_to='media/')),
                ('img6', models.ImageField(upload_to='media/')),
                ('img7', models.ImageField(upload_to='media/')),
                ('img8', models.ImageField(upload_to='media/')),
                ('img9', models.ImageField(upload_to='media/')),
                ('img10', models.ImageField(upload_to='media/')),
            ],
        ),
    ]