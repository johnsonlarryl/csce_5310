from fast_food_nutrition.analysis import ZTest
from fast_food_nutrition.model import Test


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


