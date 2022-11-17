# Generated by Django 4.1.3 on 2022-11-17 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='section',
            name='threads',
        ),
        migrations.AddField(
            model_name='section',
            name='threads',
            field=models.ManyToManyField(related_name='threads', to='forum.thread'),
        ),
    ]
