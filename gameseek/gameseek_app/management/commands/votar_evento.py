from lib2to3.pytree import Base
from django.core.management.base import BaseCommand, CommandError
from gameseek_app.models import Question as Event

class Command(BaseCommand):
    help = "Closes the specified event for voting"

    def add_arguments(self, parser) -> None:
        parser.add_argument('Event.names', nargs="+", type=int)

    def handle(self, *args, **options):
        for event_id in options["Event_names"]:
            try:
                event = Event.objects.get(pk=event_id)
            except Event.DoesNotExist:
                raise CommandError("Event "%" does not exist" % event_id)

            event.opened = False
            event.save()

            self.stdout.write(self.style.SUCCESS('Successfully closed event "%s"' % event_id))