import add


def test_add():
    o = add.Mathem(4, 5)
    assert o.add() == 9

    o = add.Mathem(1, 1)
    assert o.add() == 2
