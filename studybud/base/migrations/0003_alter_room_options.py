# Generated by Django 4.1 on 2022-09-07 00:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_topic_room_host_room_topic'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='room',
            options={'ordering': ['-updated', '-created']},
        ),
    ]
