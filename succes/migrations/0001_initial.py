# Generated by Django 4.0.3 on 2022-05-28 11:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('fiches', '0023_alter_charactersheet_avatar'),
    ]

    operations = [
        migrations.CreateModel(
            name='AchievementsSheet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('success_1', models.CharField(blank=True, choices=[('Oui', 'Oui'), ('Non', 'Non')], default='Oui', max_length=50, null=True)),
                ('success_2', models.CharField(blank=True, choices=[('Oui', 'Oui'), ('Non', 'Non')], default='Oui', max_length=50, null=True)),
                ('success_3', models.CharField(blank=True, choices=[('Oui', 'Oui'), ('Non', 'Non')], default='Oui', max_length=50, null=True)),
                ('success_4', models.CharField(blank=True, choices=[('Oui', 'Oui'), ('Non', 'Non')], default='Oui', max_length=50, null=True)),
                ('success_5', models.CharField(blank=True, choices=[('Oui', 'Oui'), ('Non', 'Non')], default='Oui', max_length=50, null=True)),
                ('success_6', models.CharField(blank=True, choices=[('Oui', 'Oui'), ('Non', 'Non')], default='Oui', max_length=50, null=True)),
                ('success_7', models.CharField(blank=True, choices=[('Oui', 'Oui'), ('Non', 'Non')], default='Oui', max_length=50, null=True)),
                ('success_8', models.CharField(blank=True, choices=[('Oui', 'Oui'), ('Non', 'Non')], default='Oui', max_length=50, null=True)),
                ('success_9', models.CharField(blank=True, choices=[('Oui', 'Oui'), ('Non', 'Non')], default='Oui', max_length=50, null=True)),
                ('success_10', models.CharField(blank=True, choices=[('Oui', 'Oui'), ('Non', 'Non')], default='Oui', max_length=50, null=True)),
                ('success_11', models.CharField(blank=True, choices=[('Oui', 'Oui'), ('Non', 'Non')], default='Oui', max_length=50, null=True)),
                ('success_12', models.CharField(blank=True, choices=[('Oui', 'Oui'), ('Non', 'Non')], default='Oui', max_length=50, null=True)),
                ('success_13', models.CharField(blank=True, choices=[('Oui', 'Oui'), ('Non', 'Non')], default='Oui', max_length=50, null=True)),
                ('success_14', models.CharField(blank=True, choices=[('Oui', 'Oui'), ('Non', 'Non')], default='Oui', max_length=50, null=True)),
                ('success_15', models.CharField(blank=True, choices=[('Oui', 'Oui'), ('Non', 'Non')], default='Oui', max_length=50, null=True)),
                ('success_16', models.CharField(blank=True, choices=[('Oui', 'Oui'), ('Non', 'Non')], default='Oui', max_length=50, null=True)),
                ('success_17', models.CharField(blank=True, choices=[('Oui', 'Oui'), ('Non', 'Non')], default='Oui', max_length=50, null=True)),
                ('success_18', models.CharField(blank=True, choices=[('Oui', 'Oui'), ('Non', 'Non')], default='Oui', max_length=50, null=True)),
                ('success_19', models.CharField(blank=True, choices=[('Oui', 'Oui'), ('Non', 'Non')], default='Oui', max_length=50, null=True)),
                ('success_20', models.CharField(blank=True, choices=[('Oui', 'Oui'), ('Non', 'Non')], default='Oui', max_length=50, null=True)),
                ('success_21', models.CharField(blank=True, choices=[('Oui', 'Oui'), ('Non', 'Non')], default='Oui', max_length=50, null=True)),
                ('success_22', models.CharField(blank=True, choices=[('Oui', 'Oui'), ('Non', 'Non')], default='Oui', max_length=50, null=True)),
                ('success_23', models.CharField(blank=True, choices=[('Oui', 'Oui'), ('Non', 'Non')], default='Oui', max_length=50, null=True)),
                ('success_24', models.CharField(blank=True, choices=[('Oui', 'Oui'), ('Non', 'Non')], default='Oui', max_length=50, null=True)),
                ('success_25', models.CharField(blank=True, choices=[('Oui', 'Oui'), ('Non', 'Non')], default='Oui', max_length=50, null=True)),
                ('success_26', models.CharField(blank=True, choices=[('Oui', 'Oui'), ('Non', 'Non')], default='Oui', max_length=50, null=True)),
                ('success_27', models.CharField(blank=True, choices=[('Oui', 'Oui'), ('Non', 'Non')], default='Oui', max_length=50, null=True)),
                ('success_28', models.CharField(blank=True, choices=[('Oui', 'Oui'), ('Non', 'Non')], default='Oui', max_length=50, null=True)),
                ('success_29', models.CharField(blank=True, choices=[('Oui', 'Oui'), ('Non', 'Non')], default='Oui', max_length=50, null=True)),
                ('success_30', models.CharField(blank=True, choices=[('Oui', 'Oui'), ('Non', 'Non')], default='Oui', max_length=50, null=True)),
                ('success_31', models.CharField(blank=True, choices=[('Oui', 'Oui'), ('Non', 'Non')], default='Oui', max_length=50, null=True)),
                ('success_32', models.CharField(blank=True, choices=[('Oui', 'Oui'), ('Non', 'Non')], default='Oui', max_length=50, null=True)),
                ('success_33', models.CharField(blank=True, choices=[('Oui', 'Oui'), ('Non', 'Non')], default='Oui', max_length=50, null=True)),
                ('success_34', models.CharField(blank=True, choices=[('Oui', 'Oui'), ('Non', 'Non')], default='Oui', max_length=50, null=True)),
                ('success_35', models.CharField(blank=True, choices=[('Oui', 'Oui'), ('Non', 'Non')], default='Oui', max_length=50, null=True)),
                ('success_36', models.CharField(blank=True, choices=[('Oui', 'Oui'), ('Non', 'Non')], default='Oui', max_length=50, null=True)),
                ('success_37', models.CharField(blank=True, choices=[('Oui', 'Oui'), ('Non', 'Non')], default='Oui', max_length=50, null=True)),
                ('success_38', models.CharField(blank=True, choices=[('Oui', 'Oui'), ('Non', 'Non')], default='Oui', max_length=50, null=True)),
                ('success_39', models.CharField(blank=True, choices=[('Oui', 'Oui'), ('Non', 'Non')], default='Oui', max_length=50, null=True)),
                ('success_40', models.CharField(blank=True, choices=[('Oui', 'Oui'), ('Non', 'Non')], default='Oui', max_length=50, null=True)),
                ('success_41', models.CharField(blank=True, choices=[('Oui', 'Oui'), ('Non', 'Non')], default='Oui', max_length=50, null=True)),
                ('success_42', models.CharField(blank=True, choices=[('Oui', 'Oui'), ('Non', 'Non')], default='Oui', max_length=50, null=True)),
                ('success_43', models.CharField(blank=True, choices=[('Oui', 'Oui'), ('Non', 'Non')], default='Oui', max_length=50, null=True)),
                ('success_44', models.CharField(blank=True, choices=[('Oui', 'Oui'), ('Non', 'Non')], default='Oui', max_length=50, null=True)),
                ('success_45', models.CharField(blank=True, choices=[('Oui', 'Oui'), ('Non', 'Non')], default='Oui', max_length=50, null=True)),
                ('success_46', models.CharField(blank=True, choices=[('Oui', 'Oui'), ('Non', 'Non')], default='Oui', max_length=50, null=True)),
                ('success_47', models.CharField(blank=True, choices=[('Oui', 'Oui'), ('Non', 'Non')], default='Oui', max_length=50, null=True)),
                ('success_48', models.CharField(blank=True, choices=[('Oui', 'Oui'), ('Non', 'Non')], default='Oui', max_length=50, null=True)),
                ('success_49', models.CharField(blank=True, choices=[('Oui', 'Oui'), ('Non', 'Non')], default='Oui', max_length=50, null=True)),
                ('success_50', models.CharField(blank=True, choices=[('Oui', 'Oui'), ('Non', 'Non')], default='Oui', max_length=50, null=True)),
                ('success_51', models.CharField(blank=True, choices=[('Oui', 'Oui'), ('Non', 'Non')], default='Oui', max_length=50, null=True)),
                ('success_52', models.CharField(blank=True, choices=[('Oui', 'Oui'), ('Non', 'Non')], default='Oui', max_length=50, null=True)),
                ('success_53', models.CharField(blank=True, choices=[('Oui', 'Oui'), ('Non', 'Non')], default='Oui', max_length=50, null=True)),
                ('success_54', models.CharField(blank=True, choices=[('Oui', 'Oui'), ('Non', 'Non')], default='Oui', max_length=50, null=True)),
                ('success_55', models.CharField(blank=True, choices=[('Oui', 'Oui'), ('Non', 'Non')], default='Oui', max_length=50, null=True)),
                ('success_56', models.CharField(blank=True, choices=[('Oui', 'Oui'), ('Non', 'Non')], default='Oui', max_length=50, null=True)),
                ('success_57', models.CharField(blank=True, choices=[('Oui', 'Oui'), ('Non', 'Non')], default='Oui', max_length=50, null=True)),
                ('success_58', models.CharField(blank=True, choices=[('Oui', 'Oui'), ('Non', 'Non')], default='Oui', max_length=50, null=True)),
                ('success_59', models.CharField(blank=True, choices=[('Oui', 'Oui'), ('Non', 'Non')], default='Oui', max_length=50, null=True)),
                ('success_60', models.CharField(blank=True, choices=[('Oui', 'Oui'), ('Non', 'Non')], default='Oui', max_length=50, null=True)),
                ('success_61', models.CharField(blank=True, choices=[('Oui', 'Oui'), ('Non', 'Non')], default='Oui', max_length=50, null=True)),
                ('success_62', models.CharField(blank=True, choices=[('Oui', 'Oui'), ('Non', 'Non')], default='Oui', max_length=50, null=True)),
                ('success_63', models.CharField(blank=True, choices=[('Oui', 'Oui'), ('Non', 'Non')], default='Oui', max_length=50, null=True)),
                ('success_64', models.CharField(blank=True, choices=[('Oui', 'Oui'), ('Non', 'Non')], default='Oui', max_length=50, null=True)),
                ('success_65', models.CharField(blank=True, choices=[('Oui', 'Oui'), ('Non', 'Non')], default='Oui', max_length=50, null=True)),
                ('success_66', models.CharField(blank=True, choices=[('Oui', 'Oui'), ('Non', 'Non')], default='Oui', max_length=50, null=True)),
                ('success_67', models.CharField(blank=True, choices=[('Oui', 'Oui'), ('Non', 'Non')], default='Oui', max_length=50, null=True)),
                ('success_68', models.CharField(blank=True, choices=[('Oui', 'Oui'), ('Non', 'Non')], default='Oui', max_length=50, null=True)),
                ('success_69', models.CharField(blank=True, choices=[('Oui', 'Oui'), ('Non', 'Non')], default='Oui', max_length=50, null=True)),
                ('success_70', models.CharField(blank=True, choices=[('Oui', 'Oui'), ('Non', 'Non')], default='Oui', max_length=50, null=True)),
                ('success_71', models.CharField(blank=True, choices=[('Oui', 'Oui'), ('Non', 'Non')], default='Oui', max_length=50, null=True)),
                ('success_72', models.CharField(blank=True, choices=[('Oui', 'Oui'), ('Non', 'Non')], default='Oui', max_length=50, null=True)),
                ('success_73', models.CharField(blank=True, choices=[('Oui', 'Oui'), ('Non', 'Non')], default='Oui', max_length=50, null=True)),
                ('success_74', models.CharField(blank=True, choices=[('Oui', 'Oui'), ('Non', 'Non')], default='Oui', max_length=50, null=True)),
                ('success_75', models.CharField(blank=True, choices=[('Oui', 'Oui'), ('Non', 'Non')], default='Oui', max_length=50, null=True)),
                ('success_76', models.CharField(blank=True, choices=[('Oui', 'Oui'), ('Non', 'Non')], default='Oui', max_length=50, null=True)),
                ('success_77', models.CharField(blank=True, choices=[('Oui', 'Oui'), ('Non', 'Non')], default='Oui', max_length=50, null=True)),
                ('success_78', models.CharField(blank=True, choices=[('Oui', 'Oui'), ('Non', 'Non')], default='Oui', max_length=50, null=True)),
                ('success_79', models.CharField(blank=True, choices=[('Oui', 'Oui'), ('Non', 'Non')], default='Oui', max_length=50, null=True)),
                ('success_80', models.CharField(blank=True, choices=[('Oui', 'Oui'), ('Non', 'Non')], default='Oui', max_length=50, null=True)),
                ('success_81', models.CharField(blank=True, choices=[('Oui', 'Oui'), ('Non', 'Non')], default='Oui', max_length=50, null=True)),
                ('success_82', models.CharField(blank=True, choices=[('Oui', 'Oui'), ('Non', 'Non')], default='Oui', max_length=50, null=True)),
                ('success_83', models.CharField(blank=True, choices=[('Oui', 'Oui'), ('Non', 'Non')], default='Oui', max_length=50, null=True)),
                ('success_84', models.CharField(blank=True, choices=[('Oui', 'Oui'), ('Non', 'Non')], default='Oui', max_length=50, null=True)),
                ('success_85', models.CharField(blank=True, choices=[('Oui', 'Oui'), ('Non', 'Non')], default='Oui', max_length=50, null=True)),
                ('success_86', models.CharField(blank=True, choices=[('Oui', 'Oui'), ('Non', 'Non')], default='Oui', max_length=50, null=True)),
                ('success_87', models.CharField(blank=True, choices=[('Oui', 'Oui'), ('Non', 'Non')], default='Oui', max_length=50, null=True)),
                ('success_88', models.CharField(blank=True, choices=[('Oui', 'Oui'), ('Non', 'Non')], default='Oui', max_length=50, null=True)),
                ('success_89', models.CharField(blank=True, choices=[('Oui', 'Oui'), ('Non', 'Non')], default='Oui', max_length=50, null=True)),
                ('success_90', models.CharField(blank=True, choices=[('Oui', 'Oui'), ('Non', 'Non')], default='Oui', max_length=50, null=True)),
                ('owner', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='fiches.charactersheet')),
            ],
            options={
                'ordering': ['owner'],
            },
        ),
    ]
