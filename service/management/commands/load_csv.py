
import re
import pandas as pd
from django.core.management.base import BaseCommand
from loguru import logger

from service.models import Provider, Location, Nature
from service.config import (
    DEFAULT_CSV_FILE_PATH,
    CHOICES_SERVICE_LOCATIONS,
    CHOICES_SERVICE_NATURES,
)
from service.serializers import ProviderSerializer


class Command(BaseCommand):
    help = 'Load CSV data into the database'

    def add_arguments(self, parser):
        parser.add_argument('--path', type=str, default=DEFAULT_CSV_FILE_PATH, help='Path to the CSV file')
        parser.add_argument('--force', action='store_true', help='Force update or create')

    def handle(self, *args, **kwargs):

        if Provider.objects.exists():
            if not kwargs['force']:
                logger.info('Database have providers, You must specify --force to overwrite existing')
                return

        # Adding Service Locations
        for row in CHOICES_SERVICE_LOCATIONS:
            Location.objects.update_or_create(id=row['id'], name=row['name'])
        logger.success(f'Service Locations: {CHOICES_SERVICE_LOCATIONS}')

        # Adding Service Nature
        for row in CHOICES_SERVICE_NATURES:
            Nature.objects.update_or_create(id=row['id'], name=row['name'], type=row['type'])
        logger.success(f'Service Natures: {CHOICES_SERVICE_NATURES}')

        # Adding CSV Data
        csv_file_path = kwargs['path']
        df = pd.read_csv(csv_file_path)

        updated_count = 0
        created_count = 0

        for index, row in df.iterrows():

            object, created = Provider.objects.update_or_create(
                id=row['Id'],
                listings_name=row['ListingsName'],
                service_location= Location.objects.filter(name=row['ServiceLocation']).first(),
                price_per_hour=float(re.search(r'\d+\.?\d*', row['PricePerHour']).group()),
                service_nature=Nature.objects.filter(name=row['ServiceNature']).first(),
                service_name=row['ProviderName'],
            )

            if created:
                created_count += 1
                logger.success(f"Added: {ProviderSerializer(object).data}")

            else:
                updated_count += 1
                logger.info(f"Updated: {ProviderSerializer(object).data}")

        logger.info('CSV data loaded/updated successfully')
        logger.info(f'Total rows updated: {updated_count} & added: {created_count}')

