# Generated by Django 4.2.4 on 2024-07-30 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0037_vacancy_hired'),
    ]

    operations = [
        migrations.CreateModel(
            name='ThanksMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
            ],
        ),
    ]
