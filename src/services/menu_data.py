import csv
from models.dish import Dish
from models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = self.make_menu(source_path)

    def make_menu(self, source_path: str):
        dishes = {}
        with open(source_path, encoding="utf8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                dish_name = row["dish"]
                if dish_name not in dishes:
                    dishes[dish_name] = Dish(dish_name, float(row["price"]))

                dishes[dish_name].add_ingredient_dependency(
                    Ingredient(row["ingredient"]), int(row["recipe_amount"])
                )

        return dishes.values()
