# Generated by Django 4.0.1 on 2022-01-26 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_student_created_at_student_first_name_student_gender_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='phone_number',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
    ]