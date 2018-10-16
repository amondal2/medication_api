# Generated by Django 2.1 on 2018-10-15 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('medications', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=155)),
                ('age', models.IntegerField(blank=True, default=1, null=True)),
                ('medications', models.ManyToManyField(to='medications.Medication')),
            ],
        ),
    ]
