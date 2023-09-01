from django.test import TestCase
from .models import Person
# Create your tests here.

class PersonModelTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        cls.person = Person.objects.create(
            name="Christson",
            age=22,
            semestre="first"
        )

    def test_field(self):
        self.assertIsInstance(self.person.name, str)
        self.assertIsInstance(self.person.age, int)
