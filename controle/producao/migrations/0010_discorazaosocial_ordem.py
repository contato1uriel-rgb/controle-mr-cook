from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("producao", "0009_discorazaosocial_full_layout"),
    ]

    operations = [
        migrations.AddField(
            model_name="discorazaosocial",
            name="ordem",
            field=models.PositiveIntegerField(default=0),
        ),
    ]
