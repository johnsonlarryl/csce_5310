from abc import ABC, abstractmethod
import numpy as np
import pandas as pd
from pandas import DataFrame

from fast_food_nutrition.model import FoodNutritionFeatures
from fast_food_nutrition.util import get_full_qualified_file_name


class FastFoodMenuETL(ABC):
    @abstractmethod
    def load_menu_items(self) -> DataFrame: pass


class StarbucksMenuETL(FastFoodMenuETL):
    def __init__(self):
        self.BASE_DIR = "starbucks"
        self.DRINKS_FILE_NAME = f"{self.BASE_DIR}/starbucks-menu-nutrition-drinks.csv"
        self.FOOD_FILE_NAME = f"{self.BASE_DIR}/starbucks-menu-nutrition-food.csv"
        self.EXPANDED_MENU_FILE = f"{self.BASE_DIR}/starbucks_drinkMenu_expanded.csv"
        self.FOOD_AND_DRINK_COLUMNS = ["Unnamed: 0",
                                       "Calories",
                                       "Fat (g)",
                                       "Carb. (g)",
                                       "Fiber (g)",
                                       "Protein",
                                       "Protein (g)",
                                       "Total Fat (g)",
                                       "Total Carbohydrates (g)",
                                       "Dietary Fibre (g)",
                                       "Protein (g)"]
        self.DRINK_DROP_COLUMNS = ["Sodium"]
        self.DRINK_EXPANDED_DROP_COLUMNS = ['Beverage_category',
                                            'Beverage',
                                            'Beverage_prep',
                                            'Trans Fat (g)',
                                            'Saturated Fat (g)',
                                            'Sodium (mg)',
                                            'Cholesterol (mg)',
                                            'Sugars (g)',
                                            'Vitamin A (% DV)',
                                            'Vitamin C (% DV)',
                                            'Calcium (% DV)',
                                            'Iron (% DV)',
                                            'Caffeine (mg)']

    def load_menu_items(self) -> DataFrame:
        return pd.concat(self.transform_starbucks_drinks(), ignore_index=True)

    def extract_starbucks_drinks(self) -> DataFrame:
        return pd.read_csv(get_full_qualified_file_name(self.DRINKS_FILE_NAME), index_col=False)

    def transform_starbucks_drinks(self) -> DataFrame:
        starbucks_drinks = self.extract_starbucks_drinks()

        starbucks_drinks = starbucks_drinks[~(starbucks_drinks[self.FOOD_AND_DRINK_COLUMNS[1:6]] == "-").all(axis=1)]

        starbucks_drinks.rename(columns={self.FOOD_AND_DRINK_COLUMNS[0]: FoodNutritionFeatures.NAME.value,
                                         self.FOOD_AND_DRINK_COLUMNS[1]: FoodNutritionFeatures.CALORIES.value,
                                         self.FOOD_AND_DRINK_COLUMNS[2]: FoodNutritionFeatures.FAT.value,
                                         self.FOOD_AND_DRINK_COLUMNS[3]: FoodNutritionFeatures.CARBOHYDRATES.value,
                                         self.FOOD_AND_DRINK_COLUMNS[4]: FoodNutritionFeatures.FIBER.value,
                                         self.FOOD_AND_DRINK_COLUMNS[5]: FoodNutritionFeatures.PROTEIN.value}, inplace=True)

        starbucks_drinks.drop(columns=self.DRINK_DROP_COLUMNS, inplace=True)

        return starbucks_drinks

    def extract_starbucks_food(self) -> DataFrame:
        return pd.read_csv(get_full_qualified_file_name(self.FOOD_FILE_NAME),
                           encoding='utf-16',
                           index_col=False)

    def transform_starbucks_food(self) -> DataFrame:
        starbucks_food = self.extract_starbucks_food()

        starbucks_food.rename(columns={self.FOOD_AND_DRINK_COLUMNS[0]: FoodNutritionFeatures.NAME.value,
                                       self.FOOD_AND_DRINK_COLUMNS[1]: FoodNutritionFeatures.CALORIES.value,
                                       self.FOOD_AND_DRINK_COLUMNS[2]: FoodNutritionFeatures.FAT.value,
                                       self.FOOD_AND_DRINK_COLUMNS[3]: FoodNutritionFeatures.CARBOHYDRATES.value,
                                       self.FOOD_AND_DRINK_COLUMNS[4]: FoodNutritionFeatures.FIBER.value,
                                       self.FOOD_AND_DRINK_COLUMNS[6]: FoodNutritionFeatures.PROTEIN.value},
                              inplace=True)

        return starbucks_food

    def extract_starbucks_expanded_drinks(self) -> DataFrame:
        return pd.read_csv(get_full_qualified_file_name(self.EXPANDED_MENU_FILE),
                           index_col=False)

    def transform_starbucks_expanded_drinks(self) -> DataFrame:
        starbucks_drinks_expanded = self.extract_starbucks_expanded_drinks()

        starbucks_drinks_expanded.rename(columns={self.FOOD_AND_DRINK_COLUMNS[0]: FoodNutritionFeatures.NAME.value,
                                                  self.FOOD_AND_DRINK_COLUMNS[1]: FoodNutritionFeatures.CALORIES.value,
                                                  self.FOOD_AND_DRINK_COLUMNS[7]: FoodNutritionFeatures.FAT.value,
                                                  self.FOOD_AND_DRINK_COLUMNS[8]: FoodNutritionFeatures.CARBOHYDRATES.value,
                                                  self.FOOD_AND_DRINK_COLUMNS[9]: FoodNutritionFeatures.FIBER.value,
                                                  self.FOOD_AND_DRINK_COLUMNS[10]: FoodNutritionFeatures.PROTEIN.value},
                                         inplace=True)

        starbucks_drinks_expanded.drop(columns=self.DRINK_EXPANDED_DROP_COLUMNS, inplace=True)

        return starbucks_drinks_expanded






