from fast_food_nutrition.analysis import ZTest
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

    expect_z = -0.56
    expect_p_value = 0.712

    actual_z, actual_p_value = ZTest.calculate_proportion(p0=p0, x=x, n=n, test=Test.RIGHT_TAILED)

    assert actual_z == expect_z
    assert actual_p_value == expect_p_value


def test_calculate_proportion_left_tailed():
    x = 33
    n = 362
    p0 = 0.1

    expect_z = -0.56
    expect_p_value = 0.288

    actual_z, actual_p_value = ZTest.calculate_proportion(p0=p0, x=x, n=n, test=Test.LEFT_TAILED)

    assert actual_z == expect_z
    assert actual_p_value == expect_p_value


def test_calculate_proportion_hypothesis_critical_test_method_two_tailed_test_reject_h0():
    z = -0.56
    alpha = 0.05

    expect_hypothesis_test_conclusion = HypothesisTestConclusion.FAIL_TO_REJECT_H0
    actual_hypothesis_test_conclusion = ZTest.calculate_proportion_hypothesis_critical_value_test_method(z=z,
                                                                                                         alpha=alpha,
                                                                                                         test=Test.TWO_TAILED)

    assert actual_hypothesis_test_conclusion == expect_hypothesis_test_conclusion


def test_calculate_proportion_hypothesis_critical_test_method_left_tailed_fail_to_reject_h0():
    z = -0.56
    alpha = 0.05

    expect_hypothesis_test_conclusion = HypothesisTestConclusion.FAIL_TO_REJECT_H0
    actual_hypothesis_test_conclusion = ZTest.calculate_proportion_hypothesis_critical_value_test_method(z=z,
                                                                                                         alpha=alpha,
                                                                                                         test=Test.LEFT_TAILED)

    assert actual_hypothesis_test_conclusion == expect_hypothesis_test_conclusion


def test_calculate_proportion_hypothesis_critical_test_method_right_tailed_fail_to_reject_h0():
    z = -0.56
    alpha = 0.05

    expect_hypothesis_test_conclusion = HypothesisTestConclusion.FAIL_TO_REJECT_H0
    actual_hypothesis_test_conclusion = ZTest.calculate_proportion_hypothesis_critical_value_test_method(z=z,
                                                                                                         alpha=alpha,
                                                                                                         test=Test.RIGHT_TAILED)

    assert actual_hypothesis_test_conclusion == expect_hypothesis_test_conclusion


def test_calculate_proportion_hypothesis_p_value_test_method_reject_h0():
    p_value = 0.288
    alpha = 0.05

    expect_hypothesis_test_conclusion = HypothesisTestConclusion.FAIL_TO_REJECT_H0
    actual_hypothesis_test_conclusion = ZTest.calculate_proportion_hypothesis_p_value_test_method(p_value=p_value,
                                                                                                  alpha=alpha)

    assert actual_hypothesis_test_conclusion == expect_hypothesis_test_conclusion





