# Generated by Django 5.2.1 on 2025-06-17 09:39

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventapp', '0010_usersuggestion_rename_full_name_usermessage_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersuggestion',
            name='submitted_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
