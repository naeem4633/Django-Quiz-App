# Generated by Django 4.1.7 on 2023-03-30 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_remove_question_question_choice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='is_gay',
        ),
        migrations.AddField(
            model_name='question',
            name='question_choice',
            field=models.BooleanField(null=True),
        ),
    ]
