from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from flower.models import login

class Command(BaseCommand):
    help = 'Create a superuser for Django admin and also create corresponding login record'

    def add_arguments(self, parser):
        parser.add_argument('--username', type=str, required=True, help='Username for the superuser')
        parser.add_argument('--email', type=str, required=True, help='Email for the superuser')
        parser.add_argument('--password', type=str, required=True, help='Password for the superuser')

    def handle(self, *args, **options):
        username = options['username']
        email = options['email']
        password = options['password']

        try:
            # Create Django superuser
            if User.objects.filter(username=username).exists():
                self.stdout.write(
                    self.style.WARNING(f'User {username} already exists in Django admin')
                )
            else:
                user = User.objects.create_superuser(username=username, email=email, password=password)
                self.stdout.write(
                    self.style.SUCCESS(f'Successfully created Django superuser: {username}')
                )

            # Create corresponding login record in custom login table
            if login.objects.filter(username=username).exists():
                self.stdout.write(
                    self.style.WARNING(f'Login record for {username} already exists in custom login table')
                )
            else:
                login.objects.create(username=username, password=password, role='admin')
                self.stdout.write(
                    self.style.SUCCESS(f'Successfully created login record for: {username}')
                )

        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Error creating superuser: {str(e)}')
            ) 