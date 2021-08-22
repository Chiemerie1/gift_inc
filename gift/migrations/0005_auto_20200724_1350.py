# Generated by Django 3.0.6 on 2020-07-24 12:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gift', '0004_giftingandrecieving'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gifting',
            fields=[
                ('gifting', models.PositiveSmallIntegerField(choices=[(1, 'first payment'), (2, 'second payment'), (3, 'THIRD payment'), (4, 'FOURTH payment'), (5, 'FIFTH PAYMENT')], verbose_name='Withdraw Frequecy')),
                ('username', models.CharField(blank=True, max_length=200)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Receiving',
            fields=[
                ('receiver', models.PositiveSmallIntegerField(choices=[(1, 'recieving one'), (2, 'recieving two'), (3, 'recieving three'), (4, 'recieving four'), (5, 'recieving five')], verbose_name='Withdraw Frequecy')),
                ('username', models.CharField(blank=True, max_length=200)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='GiftingAndRecieving',
        ),
    ]