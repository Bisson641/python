# Generated by Django 4.2.3 on 2023-07-18 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_alter_orderpaymantdetails_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='archived',
            field=models.BooleanField(default=False),
        ),
    ]
