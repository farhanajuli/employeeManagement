# Generated by Django 3.2 on 2023-12-07 06:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('emp_app', '0015_remove_project_first_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='dept',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='emp_app.department'),
        ),
    ]