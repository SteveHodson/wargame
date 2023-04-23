import pytest

from src.tables.combat import CombatTables
from src.tables.constants import Nation

def test_ground_cbt_results():
    ct = CombatTables()
    r = ct.ground_cbt_result('AE')
    assert 'Eliminated' is r[0]
    r = ct.ground_cbt_result('QR')
    assert 'Quartered' is r[0]
    r = ct.ground_cbt_result('DH')
    assert 'Halved' is r[1]
    # now use an non-existent combat code
    with pytest.raises(KeyError):
        assert ct.ground_cbt_result('ZZ') 

def test_ground_cev():
    ct = CombatTables()
    assert 1.5 == ct.ground_cev('1941', Nation.GERMANY)
    # now use an incorrect year
    with pytest.raises(KeyError):
        assert ct.ground_cev('1942', Nation.GERMANY)

def test_ratio():
    ct = CombatTables()
    # check when Attack == Defense
    a = d = 25
    assert 3 == ct._ratio(a,d)
    # 4:2 odds with a die roll == 10
    a = 4
    d = 2
    assert 4 == ct._ratio(a,d,10)
    # 2:12 odds with a die roll == 10
    a = 2
    d = 12
    assert 0 == ct._ratio(a,d,10)
    # 2:3 odds with a die roll == 10
    a = 2
    d = 3
    assert 2 == ct._ratio(a,d,10)

def test_ground_combat_resolution_table():
    ct = CombatTables()
    assert 'HX' is ct.ground_combat_resolution_table(4, 2, -2, 10)
    assert 'AQ' is ct.ground_combat_resolution_table(2, 6, -6, 10)
    assert 'DE' is ct.ground_combat_resolution_table(5, 2, 2, 10)