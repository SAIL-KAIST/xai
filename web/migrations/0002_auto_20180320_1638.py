# Generated by Django 2.0.3 on 2018-03-20 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='autonews',
            name='writer',
        ),
        migrations.AddField(
            model_name='autonews',
            name='prediction',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
