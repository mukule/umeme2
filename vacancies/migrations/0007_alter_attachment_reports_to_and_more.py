# Generated by Django 4.2.3 on 2023-08-21 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0006_alter_attachment_min_educational_level_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachment',
            name='reports_to',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='internship',
            name='reports_to',
            field=models.CharField(max_length=255),
        ),
    ]
