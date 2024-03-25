import matplotlib.pyplot as plt
from pandas import DataFrame
from typing import Dict

from fast_food_nutrition.model import COLOR, COLORS, FoodNutritionFeatures, FoodNutritionMapping


class FastFoodNutritionVisualizer:

    @staticmethod
    def generate_scatter_plots(menu: DataFrame):
        menu = FastFoodNutritionVisualizer.filter_menu(menu)

        variables = menu.columns
        n = len(variables)

        fig, axes = plt.subplots(nrows=n, ncols=n, figsize=(15, 15))

        for i, var1 in enumerate(variables):
            for j, var2 in enumerate(variables):
                if i == j:  # Diagonal: Plot a histogram
                    axes[i, j].hist(menu[var1], color=[FoodNutritionMapping[var1][COLOR]])
                else:  # Off-diagonal: Plot scatter
                    axes[i, j].scatter(menu[var2], menu[var1], color=[FoodNutritionMapping[var1][COLOR]])
                if j == 0:  # Y-axis labels only on the first column
                    axes[i, j].set_ylabel(var1)
                if i == n - 1:  # X-axis labels only on the last row
                    axes[i, j].set_xlabel(var2)
                if i < n - 1:  # Remove x-axis labels for all but the last row
                    axes[i, j].set_xticklabels([])
                if j > 0:  # Remove y-axis labels for all but the first column
                    axes[i, j].set_yticklabels([])

        plt.tight_layout()
        plt.show()

    @staticmethod
    def generate_box_plot(menu, merge=False):
        variables = menu.columns
        n = len(variables)

        if merge:
            plt.figure(figsize=(20, 5))
            plt.boxplot([menu[column] for column in variables], labels=variables, patch_artist=True)
            plt.grid(True)
        else:
            fig, axes = plt.subplots(1, n, figsize=(20, 5))

            for i, (ax, column) in enumerate(zip(axes, variables)):
                boxplot = ax.boxplot(menu[column], patch_artist=True)
                color = FoodNutritionMapping[column][COLOR]

                for median in boxplot['medians']:
                    median.set_color(color)

                for flier in boxplot['fliers']:
                    flier.set_marker('o')
                    flier.set_markerfacecolor(color)
                    flier.set_markeredgecolor('black')

                ax.set_title(column)
                ax.grid(True)

        plt.tight_layout()
        plt.show()

    @staticmethod
    def generate_histogram_plots(menu: DataFrame):
        menu = FastFoodNutritionVisualizer.filter_menu(menu)
        variables = menu.columns
        n = len(variables)

        fig, axes = plt.subplots(1, n, figsize=(20, 5))

        for ax, column in zip(axes, variables):
            ax.hist(menu[column], color=FoodNutritionMapping[column][COLOR], bins=20, edgecolor='black')
            ax.set_title(column)
            ax.grid(True)

        plt.tight_layout()
        plt.show()

    @staticmethod
    def filter_menu(menu: DataFrame) -> DataFrame:
        if FoodNutritionFeatures.MENU_ITEM in menu.keys():
            return menu.drop(FoodNutritionFeatures.MENU_ITEM, axis=1)
        else:
            return menu



