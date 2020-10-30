# Generated by Django 3.1 on 2020-10-25 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='slug',
        ),
        migrations.AlterField(
            model_name='report',
            name='report_type',
            field=models.CharField(choices=[('', '----------'), ('nonworking', "Something isn't Working"), ('sexual-abusive', 'Sexually explicit event'), ('spam', 'Spam or scam'), ('hate-speech', 'Hate Speech'), ('violence', 'Violence or Harmful event')], default='', max_length=15),
        ),
    ]
