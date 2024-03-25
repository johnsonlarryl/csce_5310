import matplotlib.pyplot as plt
from pandas import DataFrame

from fast_food_nutrition.model import COLOR, FoodNutritionMapping


class FastFoodNutritionVisualizer:

    @staticmethod
    def generate_scatter_plots(menu: DataFrame):
        menu = FastFoodNutritionVisualizer.filter_menu(menu)
        menu.drop('menu_item', axis=1)
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
    def generate_box_plot(menu: DataFrame, merge=False):
        menu = FastFoodNutritionVisualizer.filter_menu(menu)
        variables = menu.columns
        n = len(variables)

        if merge:
            plt.figure(figsize=(20, 5))
            plt.boxplot([menu[column].dropna() for column in variables], labels=variables)
            plt.grid(True)
        else:
            fig, axes = plt.subplots(1, n, figsize=(20, 5))

            for ax, column in zip(axes, variables):
                ax.boxplot(menu[column])
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
            ax.hist(menu[column].dropna(), bins=20, edgecolor='black')
            ax.set_title(column)
            ax.grid(True)

        plt.tight_layout()
        plt.show()

    @staticmethod
    def filter_menu(menu: DataFrame) -> DataFrame:
        return menu.drop('menu_item', axis=1)
