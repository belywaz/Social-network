# Generated by Django 4.2.17 on 2024-12-27 18:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_rename_sender_coment_creator_remove_coment_receiver_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coment',
            old_name='creator',
            new_name='creater',
        ),
    ]
