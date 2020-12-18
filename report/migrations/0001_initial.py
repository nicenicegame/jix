# Generated by Django 3.1.2 on 2020-11-29 21:33

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_type', models.CharField(choices=[('', '----------'), ('non-working', "Something isn't Working"), ('sexual-abusive', 'Sexually explicit event'), ('spam', 'Spam or scam'), ('hate-speech', 'Hate Speech'), ('violence', 'Violence or Harmful event')], default='', max_length=15)),
                ('detail', models.TextField(max_length=500)),
                ('reported_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.event')),
            ],
        ),
    ]
