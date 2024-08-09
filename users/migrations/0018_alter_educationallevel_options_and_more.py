# Generated by Django 4.2.3 on 2023-08-31 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_alter_customuser_access_level'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='educationallevel',
            options={'ordering': ['index']},
        ),
        migrations.AddField(
            model_name='educationallevel',
            name='index',
            field=models.PositiveIntegerField(editable=False, null=True, unique=True),
        ),
    ]
