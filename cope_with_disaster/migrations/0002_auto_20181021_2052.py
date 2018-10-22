# Generated by Django 2.0.2 on 2018-10-21 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cope_with_disaster', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Variable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='var', max_length=50)),
                ('info', models.TextField(default='info')),
            ],
        ),
        migrations.RemoveField(
            model_name='city',
            name='state',
        ),
        migrations.RemoveField(
            model_name='dam',
            name='state',
        ),
        migrations.DeleteModel(
            name='City',
        ),
        migrations.DeleteModel(
            name='Dam',
        ),
        migrations.DeleteModel(
            name='State',
        ),
    ]
