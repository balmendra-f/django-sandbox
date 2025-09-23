from django.core.management.base import BaseCommand
import json, random
from datetime import datetime, timedelta
from faker import Faker

fake = Faker("es_CL")  

class Command(BaseCommand):
    help = 'Genera un fixture grande y realista para la biblioteca'

    def handle(self, *args, **kwargs):
        NUM_NACIONALIDADES = 10
        NUM_COMUNAS = 50
        NUM_DIRECCIONES = 200
        NUM_BIBLIOTECAS = 50
        NUM_AUTORES = 100
        NUM_LIBROS = 500
        NUM_LECTORES = 500
        NUM_PRESTAMOS = 1000

        fixture = []

        def create_fixture_item(model, pk, fields):
            return {"model": model, "pk": pk, "fields": fields}

        for i in range(1, NUM_NACIONALIDADES + 1):
            pais = fake.country()
            fixture.append(create_fixture_item(
                "biblioteca.nacionalidad",
                i,
                {"pais": pais, "nacionalidad": f"{pais}na"}
            ))

        for i in range(1, NUM_COMUNAS + 1):
            fixture.append(create_fixture_item(
                "biblioteca.comuna",
                i,
                {"codigo": f"C{i:03}", "nombre": fake.city()}
            ))

        direcciones_ids = []
        for i in range(1, NUM_DIRECCIONES + 1):
            comuna_id = random.randint(1, NUM_COMUNAS)
            fixture.append(create_fixture_item(
                "biblioteca.direccion",
                i,
                {"id_comuna": comuna_id, "calle": fake.street_name(),
                 "numero": str(random.randint(1, 300)), "departamento": fake.building_number() if random.random() < 0.5 else None}
            ))
            direcciones_ids.append(i)

        # Bibliotecas (OneToOne con Direcciones)
        direcciones_biblioteca = random.sample(direcciones_ids, NUM_BIBLIOTECAS)
        for i in range(1, NUM_BIBLIOTECAS + 1):
            fixture.append(create_fixture_item(
                "biblioteca.biblioteca",
                i,
                {"nombre": f"Biblioteca Central {i}", "id_direccion": direcciones_biblioteca[i-1]}
            ))

        # Autores
        for i in range(1, NUM_AUTORES + 1):
            nacionalidad_id = random.randint(1, NUM_NACIONALIDADES)
            fixture.append(create_fixture_item(
                "biblioteca.autor",
                i,
                {"nombre": fake.name(), "id_nacionalidad": nacionalidad_id, "bio": fake.text(max_nb_chars=200)}
            ))

        # Libros
        for i in range(1, NUM_LIBROS + 1):
            autor_id = random.randint(1, NUM_AUTORES)
            biblioteca_id = random.randint(1, NUM_BIBLIOTECAS)
            fixture.append(create_fixture_item(
                "biblioteca.libro",
                i,
                {"titulo": fake.sentence(nb_words=4), "id_autor": autor_id,
                 "paginas": random.randint(50,500), "copias": random.randint(1,5),
                 "id_biblioteca": biblioteca_id, "habilitado": True}
            ))

        # Lectores
        for i in range(1, NUM_LECTORES + 1):
            direccion_id = random.randint(1, NUM_DIRECCIONES)
            biblioteca_id = random.randint(1, NUM_BIBLIOTECAS)
            rut = f"{random.randint(1000000,99999999)}-{random.choice('0123456789k')}"
            fixture.append(create_fixture_item(
                "biblioteca.lector",
                i,
                {"rut": rut, "digito_verificador": rut.split("-")[1],
                 "nombre": fake.name(), "id_direccion": direccion_id,
                 "id_biblioteca": biblioteca_id, "habilitado": True}
            ))

        # Prestamos
        for i in range(1, NUM_PRESTAMOS + 1):
            libro_id = random.randint(1, NUM_LIBROS)
            lector_id = random.randint(1, NUM_LECTORES)
            fecha_prestamo = datetime.now() - timedelta(days=random.randint(0,365))
            plazo_devolucion = fecha_prestamo + timedelta(days=14)
            fecha_entrega = fecha_prestamo + timedelta(days=random.randint(0,30)) if random.random() < 0.8 else None
            fixture.append(create_fixture_item(
                "biblioteca.prestamo",
                i,
                {"id_libro": libro_id, "id_lector": lector_id,
                 "fecha_prestamo": fecha_prestamo.isoformat(),
                 "plazo_devolucion": plazo_devolucion.isoformat(),
                 "fecha_entrega": fecha_entrega.isoformat() if fecha_entrega else None}
            ))

        with open("biblioteca/fixtures/large_fixture_realistic.json", "w", encoding="utf-8") as f:
            json.dump(fixture, f, ensure_ascii=False, indent=2)

        self.stdout.write(self.style.SUCCESS('Fixture realista generado correctamente.'))
