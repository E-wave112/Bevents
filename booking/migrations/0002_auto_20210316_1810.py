# Generated by Django 2.2 on 2021-03-16 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='eventuserprofile',
            old_name='email_adress',
            new_name='email_address',
        ),
        migrations.RenameField(
            model_name='organizerprofile',
            old_name='email_adress',
            new_name='email_address',
        ),
        migrations.AlterField(
            model_name='organizerprofile',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=100),
        ),
    ]
