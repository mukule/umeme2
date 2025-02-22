# Generated by Django 4.2.4 on 2024-08-10 11:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vacancies', '0039_terms_term_type_delete_useracceptedterms'),
    ]

    operations = [
        migrations.AlterField(
            model_name='terms',
            name='term_type',
            field=models.CharField(choices=[('external', 'External'), ('internal', 'Internal')], default='external', max_length=10),
        ),
        migrations.CreateModel(
            name='UserAcceptedTerms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accepted', models.BooleanField(default=False)),
                ('accepted_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
