# Generated by Django 5.0.1 on 2024-02-06 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slider_title', models.CharField(max_length=200)),
                ('slider_description', models.CharField(max_length=200)),
                ('slider_image', models.ImageField(blank=True, null=True, upload_to='slider/')),
            ],
        ),
    ]
