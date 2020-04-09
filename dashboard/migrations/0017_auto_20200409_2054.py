# Generated by Django 3.0.4 on 2020-04-09 20:54

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0016_auto_20200404_2005'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo_id', models.IntegerField(default=0)),
                ('file_path', models.ImageField(default='/media/custodian_pics/mylog14-03_YSaAO0C.png', upload_to='media/custodian_pics')),
            ],
        ),
        migrations.CreateModel(
            name='Snapshot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('latitude', models.FloatField(default=0.0)),
                ('longitude', models.FloatField(default=0.0)),
                ('accuracy', models.FloatField(default=0.0)),
            ],
        ),
        migrations.RemoveField(
            model_name='measurement',
            name='accuracy',
        ),
        migrations.RemoveField(
            model_name='measurement',
            name='coughing',
        ),
        migrations.RemoveField(
            model_name='measurement',
            name='headache',
        ),
        migrations.RemoveField(
            model_name='measurement',
            name='image',
        ),
        migrations.RemoveField(
            model_name='measurement',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='measurement',
            name='longitude',
        ),
        migrations.RemoveField(
            model_name='measurement',
            name='runnyNose',
        ),
        migrations.RemoveField(
            model_name='measurement',
            name='soreThroat',
        ),
        migrations.RemoveField(
            model_name='measurement',
            name='tasteLoss',
        ),
        migrations.AddField(
            model_name='measurement',
            name='image_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='measurement',
            name='user_token',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='Condition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coughing', models.IntegerField(default=0)),
                ('headache', models.IntegerField(default=0)),
                ('runnyNose', models.IntegerField(default=0)),
                ('soreThroat', models.IntegerField(default=0)),
                ('tasteLoss', models.IntegerField(default=0)),
                ('timestamp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Measurement')),
            ],
        ),
    ]
