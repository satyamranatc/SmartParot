# Generated by Django 5.1.4 on 2024-12-26 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Subjects', '0002_alter_subjects_subjectdesc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subjects',
            name='SubjectDesc',
            field=models.TextField(),
        ),
    ]