import json
from django.core.management.base import BaseCommand
from quotes.models import Authors


class Command(BaseCommand):
    help = "Load authors from a JSON file into the database"

    def handle(self, *args, **kwargs):
        json_file = "authors.json"
        with open(json_file, "r", encoding="utf-8") as file:
            data = json.load(file)
            for item in data:
                author, created = Authors.objects.get_or_create(
                    name=item["fullname"], defaults={"bio": item["description"]}
                )
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Successfully added/updated author: {author.name}"
                    )
                )
