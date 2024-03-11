# Generated by Django 4.2.3 on 2024-02-14 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Chatbot', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='chatlog',
            fields=[
                ('chatlognr', models.IntegerField(primary_key=True, serialize=False)),
                ('session_id', models.TextField()),
                ('username', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('prompt', models.TextField()),
                ('mode', models.TextField()),
                ('response', models.TextField()),
            ],
        ),
    ]