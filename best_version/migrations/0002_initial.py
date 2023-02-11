# Generated by Django 4.1.5 on 2023-02-05 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("best_version", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Goal",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("goal_text", models.CharField(max_length=200)),
                ("goal_date", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
