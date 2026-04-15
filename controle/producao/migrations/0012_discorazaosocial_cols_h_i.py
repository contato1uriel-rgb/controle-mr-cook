from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("producao", "0011_discorazaosocial_cod_not_unique"),
    ]

    operations = [
        migrations.AddField(
            model_name="discorazaosocial",
            name="col_h",
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name="discorazaosocial",
            name="col_i",
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
