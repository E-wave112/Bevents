# Generated by Django 2.2 on 2021-05-26 21:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0008_auto_20210526_2052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organizerprofile',
            name='email_address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='auth_email', to=settings.AUTH_USER_MODEL),
        ),
    ]
