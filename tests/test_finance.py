import pytest

import finance


def test_monthly_payment_known_value():
    # $200,000 at 5% over 25 years -> about $1,169.18/month
    assert finance.monthly_payment(200_000, 5, 25) == pytest.approx(1169.18, abs=0.01)


def test_zero_interest_loan_is_simple_division():
    assert finance.monthly_payment(12_000, 0, 1) == pytest.approx(1000)


def test_schedule_length_and_final_balance():
    schedule = finance.amortization_schedule(10_000, 6, 2)
    assert len(schedule) == 24
    assert schedule[-1]["balance"] == pytest.approx(0, abs=0.01)


def test_schedule_principal_sums_to_loan_amount():
    schedule = finance.amortization_schedule(10_000, 6, 2)
    assert sum(row["principal"] for row in schedule) == pytest.approx(10_000, abs=0.01)


def test_total_interest_matches_schedule():
    schedule = finance.amortization_schedule(10_000, 6, 2)
    assert finance.total_interest(10_000, 6, 2) == pytest.approx(
        sum(row["interest"] for row in schedule), abs=0.01)


def test_future_value_compound_interest():
    # $1,000 at 5% compounded monthly for 10 years -> about $1,647.01
    assert finance.future_value(1000, 5, 10) == pytest.approx(1647.01, abs=0.01)


def test_future_value_with_contributions_beats_no_contributions():
    assert finance.future_value(1000, 5, 10, 100) > finance.future_value(1000, 5, 10)


def test_future_value_zero_rate():
    assert finance.future_value(1000, 0, 2, 100) == pytest.approx(1000 + 100 * 24)


@pytest.mark.parametrize("args", [(0, 5, 10), (1000, -1, 10), (1000, 5, 0)])
def test_invalid_loan_inputs_raise(args):
    with pytest.raises(ValueError):
        finance.monthly_payment(*args)
