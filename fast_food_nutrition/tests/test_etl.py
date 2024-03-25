from pandas import DataFrame

from fast_food_nutrition.etl import McDonaldsMenuETL, StarbucksMenuETL
from fast_food_nutrition.model import FoodNutritionFeatures

FOOD_NUTRITION_FEATURES = [nutrition.value for nutrition in FoodNutritionFeatures]

FAST_FOOD_MENU_ITEM_COUNTS = {"starbucks_drinks": 92,
                              "starbucks_food": 113,
                              "starbucks_expanded_drinks": 242,
                              "starbucks_menu": 447,
                              "mcdonalds_menu": 260}


def test_transform_starbucks_drinks():
    etl = StarbucksMenuETL()
    starbucks_drinks = etl.transform_starbucks_drinks()
    assert_menu_items(starbucks_drinks, "starbucks_drinks")


def test_transform_starbucks_food():
    etl = StarbucksMenuETL()
    starbucks_drinks = etl.transform_starbucks_food()
    assert_menu_items(starbucks_drinks, "starbucks_food")


def test_transform_starbucks_expanded_drinks():
    etl = StarbucksMenuETL()
    starbucks_expanded_drinks = etl.transform_starbucks_expanded_drinks()
    assert_menu_items(starbucks_expanded_drinks, "starbucks_expanded_drinks")


def test_load_starbucks_menu_items():
    etl = StarbucksMenuETL()
    starbucks_menu = etl.load_menu_items()
    assert_menu_items(starbucks_menu, "starbucks_menu")


def test_load_mcdonalds_menu_items():
    etl = McDonaldsMenuETL()
    mdonalds_menu = etl.load_menu_items()
    assert_menu_items(mdonalds_menu, "mcdonalds_menu")


def assert_menu_items(food_menu_items: DataFrame, menu_item: str) -> None:
    for feature in food_menu_items.columns:
        assert feature in FOOD_NUTRITION_FEATURES

    assert FAST_FOOD_MENU_ITEM_COUNTS[menu_item] == len(food_menu_items)





