# Generated by Django 4.1.7 on 2023-03-11 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_lod_option2'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='option2',
            field=models.CharField(choices=[('👍', '👍'), ('👎', '👎')], max_length=35, null=True),
        ),
    ]
