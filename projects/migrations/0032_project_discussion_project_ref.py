# Generated by Django 2.0.3 on 2018-03-30 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0031_auto_20180330_1119'),
    ]

    operations = [
        migrations.AddField(
            model_name='project_discussion',
            name='project_ref',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]