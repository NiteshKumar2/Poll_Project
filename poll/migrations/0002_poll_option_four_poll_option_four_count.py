# Generated by Django 4.0.6 on 2022-07-11 21:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='poll',
            name='option_four',
            field=models.CharField(default=django.utils.timezone.now, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='poll',
            name='option_four_count',
            field=models.IntegerField(default=0),
        ),
    ]
