# Generated by Django 3.0.8 on 2020-10-07 07:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mywebsite', '0005_lesson_section'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='lesson_type',
            field=models.CharField(choices=[('free', 'free'), ('paid', 'paid')], default='paid', max_length=100),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='section',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mywebsite.Section'),
        ),
    ]
