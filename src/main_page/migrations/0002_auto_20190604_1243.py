# Generated by Django 2.2.1 on 2019-06-04 07:13

from django.db import migrations, models
import main_page.validators


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Siteuser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=25, validators=[main_page.validators.validate_username_length, main_page.validators.validate_username_alphadigits], verbose_name='User name')),
                ('password1', models.CharField(max_length=30, validators=[main_page.validators.validate_password_length, main_page.validators.validate_password_digit, main_page.validators.validate_password_uppercase])),
                ('password2', models.CharField(max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]