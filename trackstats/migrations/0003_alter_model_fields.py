# Generated by Django 3.2.17 on 2023-02-16 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("trackstats", "0002_alter_domain_id_alter_metric_id_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="domain",
            name="id",
            field=models.AutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="metric",
            name="id",
            field=models.AutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="statisticbydate",
            name="id",
            field=models.AutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="statisticbydateandobject",
            name="id",
            field=models.AutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
