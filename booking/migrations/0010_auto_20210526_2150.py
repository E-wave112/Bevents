# Generated by Django 2.2 on 2021-05-26 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0009_auto_20210526_2101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventuserprofile',
            name='email_address',
            field=models.CharField(max_length=50),
        ),
    ]
