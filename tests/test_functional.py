import pytest

from src.manager import Manager
from src.models import Parameters
from src.models import Transfer



def test_tenants_settlements_sum_equals_apartment_costs():
    manager = Manager(Parameters())
    apartment_costs = manager.get_apartment_costs('apart-polanka', 2025, 1)
    apartment_settlement = manager.get_settlement('apart-polanka', 2025, 1)
    tenants_settlements = manager.create_tenants_settlements(apartment_settlement)
    tenants_sum = sum(ts.total_due_pln for ts in tenants_settlements)

    assert tenants_sum == pytest.approx(apartment_costs)

def test_get_debtors():
    manager = Manager(Parameters())
    assert manager.get_debtors('apart-polanka', 1, 2025) == []
    manager.transfers.append(Transfer(amount_pln=1500, date='2025-02-03',
                                      settlement_year=2025, settlement_month=2, tenant='tenant-1'))
    manager.transfers.append(Transfer(amount_pln=500, date='2025-02-04',
                                      settlement_year=2025, settlement_month=2, tenant='tenant-2'))
    manager.transfers.append(Transfer(amount_pln=500, date='2025-02-10',
                                      settlement_year=2025, settlement_month=2, tenant='tenant-2'))

    debtors = manager.get_debtors('apart-polanka', 2, 2025)
    assert sorted(debtors) == ['Adam Kowalski', 'Ewa Adamska']
    assert manager.get_debtors('apartment-1', 2, 2025) is None