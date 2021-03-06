# Generated by Django 4.0.3 on 2022-04-30 16:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fiches', '0005_charactersheet_skills'),
        ('competences', '0008_alter_skill_haslevel'),
    ]

    operations = [
        migrations.CreateModel(
            name='SkillSheet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='fiches.charactersheet')),
                ('skills', models.ManyToManyField(blank=True, to='competences.skill')),
            ],
        ),
    ]
