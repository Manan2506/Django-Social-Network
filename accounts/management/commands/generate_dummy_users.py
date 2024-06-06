from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from faker import Faker


class Command(BaseCommand):
    help = 'Generate dummy user data'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of users to be created')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        fake = Faker()
        User = get_user_model()

        for _ in range(total):
            user = User(
                username=fake.user_name(),
                email=fake.email(),
                first_name=fake.first_name(),
                last_name=fake.last_name()
            )
            user.set_password('password')  # Set a default password
            user.save()

        self.stdout.write(self.style.SUCCESS(f'Successfully created {total} users'))
