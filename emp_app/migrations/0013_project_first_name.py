# Generated by Django 3.2 on 2023-12-07 05:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('emp_app', '0012_remove_employee_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='first_name',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='emp_app.employee'),
        ),
    ]