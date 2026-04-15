from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("producao", "0010_discorazaosocial_ordem"),
    ]

    operations = [
        migrations.AlterField(
            model_name="discorazaosocial",
            name="cod",
            field=models.CharField(blank=True, max_length=120),
        ),
    ]
