# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pocket', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pocket',
            name='number',
            field=models.CharField(max_length=1),
        ),
    ]
