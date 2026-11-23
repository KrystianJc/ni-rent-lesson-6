import pytest

from src.manager import Manager
from src.models import Parameters


def test_tenants_settlements_sum_equals_apartment_costs():
    manager = Manager(Parameters())
    apartment_costs = manager.get_apartment_costs('apart-polanka', 2025, 1)
    apartment_settlement = manager.get_settlement('apart-polanka', 2025, 1)
    tenants_settlements = manager.create_tenants_settlements(apartment_settlement)
    tenants_sum = sum(ts.total_due_pln for ts in tenants_settlements)

    assert tenants_sum == pytest.approx(apartment_costs)