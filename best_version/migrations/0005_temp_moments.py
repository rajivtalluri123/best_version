# Generated by Django 4.1.5 on 2023-02-05 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('best_version', '0004_bestmoment_proudmoment_version'),
    ]

    operations = [
        migrations.CreateModel(
            name='TempMoment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('temp_moment', models.CharField(max_length=500))
            ],
        ),
    ]
