# Generated by Django 5.0.1 on 2024-06-01 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="gender",
            field=models.CharField(
                choices=[("M", "男性"), ("F", "女性")], max_length=1, null=True
            ),
        ),
    ]
