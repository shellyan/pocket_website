# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pocket',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.IntegerField(default=0, max_length=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
