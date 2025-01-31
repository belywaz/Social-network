# Generated by Django 4.2.17 on 2024-12-27 16:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_rename_name_post_content'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coment',
            old_name='sender',
            new_name='creator',
        ),
        migrations.RemoveField(
            model_name='coment',
            name='receiver',
        ),
        migrations.AddField(
            model_name='coment',
            name='post',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='post_coments', to='post.post'),
            preserve_default=False,
        ),
    ]
