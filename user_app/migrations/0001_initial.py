# Generated by Django 4.1.5 on 2023-01-26 13:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vendor_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtotal', models.FloatField(default=0)),
                ('delivery_charges', models.FloatField(default=0)),
                ('tax', models.FloatField(default=0)),
                ('total', models.FloatField(default=0)),
                ('self_pickup', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='cart', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Cart',
            },
        ),
        migrations.CreateModel(
            name='CartItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('per_item_cost', models.FloatField()),
                ('total_cost', models.FloatField()),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='user_app.cart')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='vendor_app.product')),
            ],
            options={
                'db_table': 'CartItems',
            },
        ),
        migrations.CreateModel(
            name='CreditedMoney',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_balance', models.FloatField(default=0.0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='member', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('subscribed_on', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'Membership',
            },
        ),
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtotal', models.FloatField(default=0)),
                ('delivery_charges', models.FloatField(default=0)),
                ('tax', models.FloatField(default=0)),
                ('total', models.FloatField(default=0)),
                ('self_pickup', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='wishlist', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Wishlist',
            },
        ),
        migrations.CreateModel(
            name='WishlistItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('per_item_cost', models.FloatField()),
                ('total_cost', models.FloatField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wishlistproduct', to='vendor_app.product')),
                ('wishlist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='user_app.wishlist')),
            ],
            options={
                'db_table': 'WishlistItems',
            },
        ),
        migrations.CreateModel(
            name='WishlistItemVariant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_variant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendor_app.productvariant')),
                ('wishlist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_app.wishlist')),
                ('wishlistitem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_app.wishlistitems')),
            ],
            options={
                'db_table': 'WishlistItemVariant',
            },
        ),
        migrations.CreateModel(
            name='UserWithdrawRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_date', models.DateTimeField()),
                ('amount', models.FloatField()),
                ('credited_amount', models.FloatField(default=0.0)),
                ('tds', models.FloatField(default=0.0)),
                ('is_active', models.PositiveIntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='withdraw_request', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'UserWithdrawRequest',
            },
        ),
        migrations.CreateModel(
            name='UserVendorRelation',
            fields=[
                ('vendor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='vendor_app.vendor')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'UserVendorRelation',
            },
        ),
        migrations.CreateModel(
            name='UserSubscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subscrbe_on', models.DateTimeField(auto_now=True)),
                ('months', models.PositiveIntegerField(default=1)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='subscribed_usr', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'UserSubscription',
            },
        ),
        migrations.CreateModel(
            name='UserPV',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('right_pv', models.FloatField(default=0.0)),
                ('left_pv', models.FloatField(default=0.0)),
                ('level_pv', models.FloatField(default=0.0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='userpv', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'UserPV',
            },
        ),
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=50, null=True)),
                ('last_name', models.CharField(blank=True, max_length=50, null=True)),
                ('phone', models.CharField(blank=True, max_length=10, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('zipcode', models.CharField(blank=True, max_length=20, null=True)),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('longitude', models.FloatField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, max_length=20, null=True)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='profile')),
                ('pv', models.FloatField(default=0.0)),
                ('is_active', models.BooleanField(default=False)),
                ('subscribed', models.BooleanField(default=False)),
                ('sponsor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='usr', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'UserData',
            },
        ),
        migrations.CreateModel(
            name='PVTransactions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_date', models.DateTimeField()),
                ('previous_pv', models.FloatField(default=0.0)),
                ('pv', models.FloatField()),
                ('total_pv', models.FloatField()),
                ('plan', models.CharField(default='Binary', max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pv', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'PVTransactions',
            },
        ),
        migrations.CreateModel(
            name='PaymentInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_no', models.CharField(max_length=50)),
                ('bank_name', models.CharField(max_length=50)),
                ('ifsc', models.CharField(max_length=50)),
                ('pan', models.ImageField(blank=True, null=True, upload_to='payment')),
                ('aadhar', models.ImageField(blank=True, null=True, upload_to='payment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payinfo', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'PaymentInfo',
            },
        ),
        migrations.CreateModel(
            name='Memberip_Receipt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receipt_date', models.DateTimeField(auto_now=True)),
                ('razorpay_order_id', models.CharField(max_length=100)),
                ('payment_id', models.CharField(blank=True, max_length=200, null=True)),
                ('amount', models.FloatField()),
                ('is_active', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Memberip_Receipt',
            },
        ),
        migrations.CreateModel(
            name='CreditedMoneyTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_date', models.DateTimeField()),
                ('transaction_type', models.CharField(max_length=20)),
                ('transaction_amount', models.FloatField()),
                ('previous_amount', models.FloatField()),
                ('remaining_amount', models.FloatField()),
                ('creditedmoney', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_app.creditedmoney')),
            ],
        ),
        migrations.CreateModel(
            name='CartItemVariant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_app.cart')),
                ('cartitem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_app.cartitems')),
                ('product_variant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendor_app.productvariant')),
            ],
            options={
                'db_table': 'CartItemVariant',
            },
        ),
        migrations.CreateModel(
            name='Billing_Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('amount', models.FloatField(default=0.0)),
                ('plan', models.CharField(default='Level', max_length=100)),
                ('is_active', models.BooleanField(default=False)),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendor_app.store')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Billing_Request',
            },
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('name', models.CharField(max_length=100)),
                ('home_no', models.CharField(max_length=100)),
                ('landmark', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('pincode', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('address_type', models.CharField(choices=[('Home', 'Home'), ('Work', 'Work'), ('Other', 'Other')], default='Home', max_length=30)),
                ('contact', models.CharField(max_length=15)),
                ('default', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='address', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Address',
            },
        ),
    ]
