# Generated by Django 2.2.6 on 2019-10-08 00:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0004_auto_20191008_0306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='user',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
