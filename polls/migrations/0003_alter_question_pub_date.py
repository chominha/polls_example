# Generated by Django 3.2.19 on 2023-05-17 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_rename_pub_data_question_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date published'),
        ),
    ]