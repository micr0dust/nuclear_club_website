# Generated by Django 3.0.1 on 2020-02-06 09:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_auto_20200206_1708'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='post_type',
            new_name='post_typel',
        ),
    ]
