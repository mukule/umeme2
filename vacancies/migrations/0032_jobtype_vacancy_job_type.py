# Generated by Django 4.2.3 on 2024-03-08 14:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0031_remove_vacancy_vacancy_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('description', models.TextField()),
                ('banner', models.ImageField(blank=True, null=True, upload_to='job_type_banners/')),
                ('icon', models.ImageField(blank=True, null=True, upload_to='job_type_icons/')),
            ],
        ),
        migrations.AddField(
            model_name='vacancy',
            name='job_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='vacancies.jobtype'),
        ),
    ]
