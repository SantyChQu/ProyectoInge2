# Generated by Django 5.2.1 on 2025-05-23 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Maquina",
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
                ("numero_de_serie", models.CharField(max_length=100, unique=True)),
                ("marca", models.CharField(max_length=100)),
                ("modelo", models.CharField(max_length=100)),
                ("año_compra", models.PositiveIntegerField()),
                ("localidad", models.CharField(max_length=100)),
                (
                    "imagen",
                    models.ImageField(blank=True, null=True, upload_to="maquinas/"),
                ),
            ],
        ),
    ]
