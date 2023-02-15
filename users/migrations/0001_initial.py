# Generated by Django 4.1.7 on 2023-02-15 09:53

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("account", models.CharField(max_length=255)),
                ("password", models.CharField(max_length=255)),
            ],
            options={
                "db_table": "users",
            },
            managers=[
                ("manager", django.db.models.manager.Manager()),
            ],
        ),
    ]
