# Generated by Django 2.2 on 2021-05-27 19:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0011_auto_20210527_1832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organizerprofile',
            name='email_address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='auth_email', to=settings.AUTH_USER_MODEL),
        ),
    ]
