# Generated by Django 3.0.6 on 2020-10-10 07:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date created')),
                ('last_updated', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last updated')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('desc', models.TextField(default='None', max_length=500)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date created')),
                ('last_updated', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last updated')),
                ('free', models.BooleanField()),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resource.Topic')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]