# Generated by Django 2.2.1 on 2019-05-18 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("form", "0001_initial")]

    operations = [
        migrations.AddField(
            model_name="question",
            name="question",
            field=models.CharField(default="", max_length=250),
        )
    ]
