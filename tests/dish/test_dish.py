from models.ingredient import Ingredient
from src.models.dish import Dish  # noqa: F401, E261, E501
import pytest


# Req 2
def test_dish():
    dish_igual1 = Dish("Cocada", 2.00)
    dish_igual2 = Dish("Cocada", 2.00)
    dish_diferente3 = Dish("Feijoada", 12.00)

    assert dish_igual1.name == "Cocada"

    assert dish_igual1 == dish_igual2
    assert dish_igual1 != dish_diferente3

    assert repr(dish_igual1) == "Dish('Cocada', R$2.00)"

    assert hash(dish_igual1) == hash(dish_igual2)
    assert hash(dish_igual1) != hash(dish_diferente3)

    sugar = Ingredient("açucar")
    dish_igual1.add_ingredient_dependency(sugar, 1)
    assert dish_igual1.recipe == {sugar: 1}

    assert dish_diferente3.get_restrictions() == set()
    assert dish_diferente3.get_ingredients() == set()

    with pytest.raises(TypeError):
        Dish("Dish", "preço")

    with pytest.raises(ValueError):
        Dish("Dish", 0)
