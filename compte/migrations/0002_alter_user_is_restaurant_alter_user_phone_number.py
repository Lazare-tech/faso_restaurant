# Generated by Django 4.2.11 on 2024-05-04 10:11

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ("compte", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="is_restaurant",
            field=models.BooleanField(default=False, verbose_name="Est restaurant"),
        ),
        migrations.AlterField(
            model_name="user",
            name="phone_number",
            field=phonenumber_field.modelfields.PhoneNumberField(
                max_length=20, region=None, verbose_name="Numero de telephone"
            ),
        ),
    ]
