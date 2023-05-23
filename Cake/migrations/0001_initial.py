# Generated by Django 4.1.6 on 2023-03-18 14:26

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CAKE',
            fields=[
                ('cake_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('cake_name', models.CharField(max_length=20)),
                ('image', models.ImageField(upload_to='Cake_Image')),
                ('price', models.FloatField(default=1000.0, validators=[django.core.validators.MinValueValidator(1000.0), django.core.validators.MaxValueValidator(10000.0)])),
                ('color', models.CharField(choices=[('Black', 'Black'), ('White', 'White'), ('Pink', 'Pink')], max_length=10)),
            ],
            options={
                'ordering': ['flavour'],
            },
        ),
        migrations.CreateModel(
            name='CAKE_FLAVOUR',
            fields=[
                ('flavour_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('flavour_name', models.CharField(max_length=20)),
            ],
            options={
                'ordering': ['flavour_name'],
            },
        ),
        migrations.CreateModel(
            name='CAKE_PROVIDER',
            fields=[
                ('cakeprovider_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('cakep_name', models.CharField(max_length=20)),
                ('mobile', models.CharField(default=9155007890, max_length=10, validators=[django.core.validators.MinLengthValidator(10), django.core.validators.MaxLengthValidator(10)])),
                ('email', models.EmailField(default='@gmail.com', max_length=254, validators=[django.core.validators.MinLengthValidator(11), django.core.validators.MaxLengthValidator(50)])),
                ('state', models.CharField(default='Madhya Pradesh', max_length=20)),
                ('city', models.CharField(max_length=20)),
            ],
            options={
                'ordering': ['cakep_name'],
            },
        ),
        migrations.CreateModel(
            name='CAKE_WISHLIST',
            fields=[
                ('cakewish_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('cake', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cake.cake')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['user'],
            },
        ),
        migrations.CreateModel(
            name='CAKE_CART',
            fields=[
                ('cakecart_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('cake', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cake.cake')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['user'],
            },
        ),
        migrations.CreateModel(
            name='CAKE_BOOKING',
            fields=[
                ('cakeorder_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=False)),
                ('cake', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cake.cake')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['user'],
            },
        ),
        migrations.AddField(
            model_name='cake',
            name='flavour',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cake.cake_flavour'),
        ),
        migrations.AddField(
            model_name='cake',
            name='provider',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cake.cake_provider'),
        ),
    ]