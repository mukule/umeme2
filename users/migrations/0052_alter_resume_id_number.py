# Generated by Django 4.2.4 on 2024-07-28 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0051_alter_customuser_id_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='id_number',
            field=models.PositiveIntegerField(blank=True, null=True, unique=True),
        ),
    ]
