# Generated by Django 3.1.2 on 2020-11-29 21:33

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
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('description', models.TextField(max_length=500)),
                ('category', models.CharField(choices=[('', '----------'), ('eating', 'Eating'), ('sport', 'Sport'), ('party', 'Party'), ('technology', 'Technology'), ('movies', 'Movies'), ('crafts', 'Crafts'), ('business', 'Business'), ('movements', 'Movements'), ('education', 'Education')], default='', max_length=15)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('appointment_date', models.DateTimeField()),
                ('image_upload', models.ImageField(upload_to='images/')),
                ('slug', models.SlugField(allow_unicode=True, unique=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Attendee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.event')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
