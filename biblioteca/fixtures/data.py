# biblioteca/management/commands/fix_fixtures.py
import json
from django.core.management.base import BaseCommand
from django.apps import apps

class Command(BaseCommand):
    help = 'Corrige las referencias en el fixture'
    
    def handle(self, *args, **options):
        fixture_path = 'biblioteca/fixtures/initial_data.json'
        
        with open(fixture_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Reorganizar por tipo de modelo
        models_order = [
            'nacionalidad', 'autor', 'comuna', 'direccion', 
            'biblioteca', 'libro', 'lector', 'prestamo'
        ]
        
        organized_data = []
        for model_name in models_order:
            for item in data:
                if item['model'].split('.')[1] == model_name:
                    organized_data.append(item)
        
        # Guardar organizado
        with open(fixture_path, 'w', encoding='utf-8') as f:
            json.dump(organized_data, f, ensure_ascii=False, indent=2)
        
        self.stdout.write('✓ Fixture reorganizado correctamente')