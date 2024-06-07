from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("taggit", "0002_auto_20150616_2121"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="taggeditem", unique_together={("content_type", "object_id", "tag")}
        )
    ]
