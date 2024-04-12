from fast_food_nutrition.analysis import ZTest, TTest
from fast_food_nutrition.model import HypothesisTestConclusion, Test


def test_calculate_proportion_two_tailed():
    x = 33
    n = 362
    p0 = 0.1

    expect_z = -0.56
    expect_p_value = 0.575

    actual_z, actual_p_value = ZTest.calculate_proportion(p0=p0, x=x, n=n, test=Test.TWO_TAILED)

    assert actual_z == expect_z
    assert actual_p_value == expect_p_value


def test_calculate_proportion_right_tailed():
    x = 33
    n = 362
    p0 = 0.1
    test = Test.RIGHT_TAILED

    expect_z = -0.56
    expect_p_value = 0.712

    actual_z, actual_p_value = ZTest.calculate_proportion(p0=p0, x=x, n=n, test=test)

    assert actual_z == expect_z
    assert actual_p_value == expect_p_value


def test_calculate_proportion_left_tailed():
    x = 33
    n = 362
    p0 = 0.1
    test = Test.LEFT_TAILED

    expect_z = -0.56
    expect_p_value = 0.288

    actual_z, actual_p_value = ZTest.calculate_proportion(p0=p0, x=x, n=n, test=test)

    assert actual_z == expect_z
    assert actual_p_value == expect_p_value


def test_calculate_proportion_hypothesis_critical_test_method_two_tailed_test_reject_h0():
    z = -0.56
    alpha = 0.05
    test = Test.TWO_TAILED

    expect_hypothesis_test_conclusion = HypothesisTestConclusion.FAIL_TO_REJECT_H0
    actual_hypothesis_test_conclusion = ZTest.calculate_hypothesis_critical_value_test_method(z=z,
                                                                                              alpha=alpha,
                                                                                              test=test)

    assert actual_hypothesis_test_conclusion == expect_hypothesis_test_conclusion


def test_calculate_proportion_hypothesis_critical_test_method_left_tailed_fail_to_reject_h0():
    z = -0.56
    alpha = 0.05
    test = Test.LEFT_TAILED

    expect_hypothesis_test_conclusion = HypothesisTestConclusion.FAIL_TO_REJECT_H0
    actual_hypothesis_test_conclusion = ZTest.calculate_hypothesis_critical_value_test_method(z=z,
                                                                                                         alpha=alpha,
                                                                                                         test=test)

    assert actual_hypothesis_test_conclusion == expect_hypothesis_test_conclusion


def test_calculate_hypothesis_critical_test_method_right_tailed_fail_to_reject_h0():
    z = -0.56
    alpha = 0.05
    test = Test.RIGHT_TAILED

    expect_hypothesis_test_conclusion = HypothesisTestConclusion.FAIL_TO_REJECT_H0
    actual_hypothesis_test_conclusion = ZTest.calculate_hypothesis_critical_value_test_method(z=z,
                                                                                             alpha=alpha,
                                                                                             test=test)

    assert actual_hypothesis_test_conclusion == expect_hypothesis_test_conclusion


def test_calculate_p_value_test_method_reject_h0():
    p_value = 0.288
    alpha = 0.05

    expect_hypothesis_test_conclusion = HypothesisTestConclusion.FAIL_TO_REJECT_H0
    actual_hypothesis_test_conclusion = ZTest.calculate_p_value_test_method(p_value=p_value,
                                                                            alpha=alpha)

    assert actual_hypothesis_test_conclusion == expect_hypothesis_test_conclusion


def test_calculate_proporation_confidence_interval():
    x = 33
    n = 362
    alpha = 0.05
    test = Test.TWO_TAILED

    expect_confidence_interval = (0.062, 0.121)
    actual_confidence_interval = ZTest.calculate_proporation_confidence_interval(x=x,
                                                                                 n=n,
                                                                                 alpha=alpha,
                                                                                 test=test)

    assert actual_confidence_interval == expect_confidence_interval


def test_calculate_confidence_interval_test_method():
    p0 = 0.1
    min = 0.062
    max = 0.121

    expect_hypothesis_test_conclusion = HypothesisTestConclusion.FAIL_TO_REJECT_H0
    actual_hypothesis_test_conclusion = ZTest.calculate_confidence_interval_test_method(p0=p0,
                                                                                        min=min,
                                                                                        max=max)

    assert actual_hypothesis_test_conclusion == expect_hypothesis_test_conclusion


def test_calculate_mean_confidence_interval():
    x_bar = 30.9
    sigma = 2.9
    n = 15
    alpha = 0.05
    test = Test.TWO_TAILED

    expect_confidence_interval = (29.432, 32.368)
    actual_confidence_interval = ZTest.calculate_mean_confidence_interval(x_bar=x_bar,
                                                                          sigma=sigma,
                                                                          n=n,
                                                                          alpha=alpha,
                                                                          test=test)

    assert actual_confidence_interval == expect_confidence_interval


def test_calculate_mean():
    x_bar = 30.9
    sigma = 2.9
    n = 15
    mu = 40
    test = Test.TWO_TAILED

    expect_z = -12.15
    expect_p_value = 0.00

    actual_z, actual_p_value = ZTest.calculate_mean(x_bar=x_bar,
                                                    mu=mu,
                                                    sigma=sigma,
                                                    n=n,
                                                    test=test)

    assert actual_z == expect_z
    assert actual_p_value == expect_p_value


def test_calculate_two_means():
    x_bar_1 = 3.866667
    x_bar_2 = 3.993333

    # Assume mu_1 == mu_2
    mu_1 = 0
    mu_2 = 0
    sigma_1 = 0.563001
    sigma_2 = 0.39
    n_1 = 12
    n_2 = 15
    test = Test.TWO_TAILED

    expect_t = -0.66
    expect_p_value = 0.520

    actual_t, actual_p_value = TTest.calculate_two_means(x_bar_1=x_bar_1,
                                                         x_bar_2=x_bar_2,
                                                         mu_1=mu_1,
                                                         mu_2=mu_2,
                                                         sigma_1=sigma_1,
                                                         sigma_2=sigma_2,
                                                         n_1=n_1,
                                                         n_2=n_2,
                                                         test=test)

    assert actual_t == expect_t
    assert actual_p_value == expect_p_value


def test_calculate_two_means_confidence_interval():
    x_bar_1 = 3.866667
    x_bar_2 = 3.993333
    sigma_1 = 0.563001
    sigma_2 = 0.39
    n_1 = 12
    n_2 = 15
    alpha = 0.05
    test = Test.TWO_TAILED

    expect_confidence_interval = (-0.544, 0.291)
    actual_confidence_interval = TTest.calculate_two_means_confidence_interval(x_bar_1=x_bar_1,
                                                                               x_bar_2=x_bar_2,
                                                                               sigma_1=sigma_1,
                                                                               sigma_2=sigma_2,
                                                                               n_1=n_1,
                                                                               n_2=n_2,
                                                                               alpha=alpha,
                                                                               test=test)

    assert actual_confidence_interval == expect_confidence_interval





















