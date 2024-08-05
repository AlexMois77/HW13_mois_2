import json
from django.core.management.base import BaseCommand
from quotes.models import Authors, Quote, Tag


class Command(BaseCommand):
    help = "Load quotes from a JSON file into the database"

    def handle(self, *args, **kwargs):
        json_file = "quotes.json"
        with open(json_file, "r", encoding="utf-8") as file:
            data = json.load(file)
            for item in data:
                author_name = item["author"]
                quote_text = item["quote"]
                tags = item["tags"]

                author, created = Authors.objects.get_or_create(name=author_name)

                if not Quote.objects.filter(author=author, text=quote_text).exists():
                    quote = Quote.objects.create(author=author, text=quote_text)

                    for tag_name in tags:
                        tag, created = Tag.objects.get_or_create(name=tag_name)
                        quote.tags.add(tag)

                    self.stdout.write(
                        self.style.SUCCESS(
                            f'Successfully added quote: "{quote_text}" by {author.name}'
                        )
                    )
                else:
                    self.stdout.write(
                        self.style.WARNING(
                            f'Quote already exists: "{quote_text}" by {author.name}'
                        )
                    )
