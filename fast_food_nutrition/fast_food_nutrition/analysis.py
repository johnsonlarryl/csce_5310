import math

import pandas as pd
from pandas import DataFrame, Series
from scipy.stats import chi2, norm, t
from typing import List, Tuple

from fast_food_nutrition.model import HypothesisTestConclusion, HypothesisTestMethod, Test


class Outliers:
    @staticmethod
    def filter_outliers(menu: DataFrame, columns: List[str]):
        def remove_outliers(column: Series) -> DataFrame:
            Q1 = column.quantile(0.25)
            Q3 = column.quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR

            return (column >= lower_bound) & (column <= upper_bound)

        mask = pd.Series([True] * len(menu))

        for col in columns:
            mask &= remove_outliers(menu[col])

        return menu[mask]


class ZTest:
    """
    Method that runs the z-test and return the critical value and p-value
    """
    @staticmethod
    def calculate(p0: int, phat: float, n: int, level_of_significance=0.05):
        # Calculate the z-score
        z = (phat - p0) / ((p0 * (1 - p0) / n) ** level_of_significance)

        # Calculate the p-value for a right-tailed test
        p_value = norm.sf(z)  # This is the survival function, equivalent to 1 - CDF

        return z, p_value

    """
        Method that runs the z-test and return the critical value and p-value
    """
    @staticmethod
    def calculate_proportion(p0: int, x: int, n: int, test: Test) -> Tuple[float, float]:
        # Calculate the z-score
        p_hat = x / n
        z = (p_hat - p0) / math.sqrt((p0 * (1 - p0)) / n)

        if test == Test.TWO_TAILED:  # Calculate the p-value for a two-tailed test
            p_value = 2 * (1 - norm.cdf(abs(z)))
        elif test == Test.LEFT_TAILED: # Calculate the p-value for a left-tailed test
            p_value = norm.cdf(z)
        elif test == Test.RIGHT_TAILED: # Calculate the p-value for a right-tailed test
            p_value = 1 - norm.cdf(z)

        return round(z, 2), round(p_value, 3)

    @staticmethod
    def calculate_proportion_hypothesis_critical_value_test_method(z: float, alpha: float, test: Test) -> HypothesisTestConclusion:
        if test == Test.TWO_TAILED:
            z_alpha_2 = 1 - (alpha / 2)
            critical_value_lower = norm.ppf(z_alpha_2)
            critical_value_upper = norm.ppf(1 - z_alpha_2)

            if z <= critical_value_lower or z >= critical_value_upper:
                return HypothesisTestConclusion.REJECT_H_0
            else:
                return HypothesisTestConclusion.FAIL_TO_REJECT_H0
        elif test == Test.LEFT_TAILED:
            critical_value = norm.ppf(alpha)

            if z <= critical_value:
                return HypothesisTestConclusion.REJECT_H_0
            else:
                return HypothesisTestConclusion.FAIL_TO_REJECT_H0
        elif test == Test.RIGHT_TAILED:
            critical_value = norm.ppf(1 - alpha)

            if z >= critical_value:
                return HypothesisTestConclusion.REJECT_H_0
            else:
                return HypothesisTestConclusion.FAIL_TO_REJECT_H0

    @staticmethod
    def calculate_proportion_hypothesis_p_value_test_method(p_value: float, alpha: float) -> HypothesisTestConclusion: pass



class TTest:
    @staticmethod
    def calculate(x_bar: float, mu_0: float, n: int, s: float):
        # Calculate the t statistic
        t_statistic = (x_bar - mu_0) / (s / (n ** 0.5))

        # Degrees of freedom
        df = n - 1

        # Calculate the p-value for a right-tailed test
        p_value = t.sf(t_statistic, df)

        return t_statistic, p_value


class ChiSquaredTest:
    @staticmethod
    def calculate(n: int, s: float, sigma_0):
        # Calculate the chi-squared statistic
        chi_squared_statistic = ((n - 1) * s ** 2) / (sigma_0 ** 2)

        # Degrees of freedom
        df = n - 1

        # Calculate the p-value for a right-tailed test
        p_value = chi2.sf(chi_squared_statistic, df)

        return chi_squared_statistic, p_value
