# Generated by Django 3.1.3 on 2020-11-18 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('price', models.IntegerField(default=0)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('quantity', models.IntegerField(default=0)),
            ],
        ),
    ]