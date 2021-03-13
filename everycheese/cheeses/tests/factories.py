""" factories.py"""
from django.template.defaultfilters import slugify
import factory
import factory.fuzzy
import pytest
from everycheese.users.tests.factories import UserFactory
from ..models import Cheese

@pytest.fixture
def cheese():
    """cheese"""
    return CheeseFactory()

class CheeseFactory(factory.django.DjangoModelFactory):
    """ factory class"""
    name = factory.fuzzy.FuzzyText()
    slug = factory.LazyAttribute(lambda obj: slugify(obj.name))
    description = factory.Faker(
    'paragraph', nb_sentences=3, variable_nb_sentences=True
    )
    firmness = factory.fuzzy.FuzzyChoice(
    [x[0] for x in Cheese.Firmness.choices]
    )
    country_of_origin = factory.Faker('country_code')
    creator = factory.SubFactory(UserFactory)

    class Meta:
        """ class meta """
        model = Cheese
