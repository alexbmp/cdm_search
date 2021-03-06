# Generated by Django 2.0.9 on 2018-11-09 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Code',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_id', models.CharField(max_length=30)),
                ('source_name', models.CharField(max_length=150)),
                ('target_id', models.CharField(max_length=30)),
                ('target_name', models.CharField(max_length=150)),
                ('vocabulary', models.CharField(max_length=30)),
                ('domain', models.CharField(max_length=30)),
                ('target_concept', models.CharField(max_length=30)),
                ('division', models.CharField(max_length=30)),
                ('unit', models.CharField(max_length=30)),
                ('review', models.CharField(max_length=250)),
                ('other', models.CharField(max_length=100)),
            ],
        ),
    ]
