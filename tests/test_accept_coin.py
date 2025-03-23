from app.vending_machine import VendingMachine, Coin


def test_when_a_valid_coin_is_inserted_add_to_current_amount():
    vending_machine = VendingMachine()

    actual = vending_machine.insert_coin(Coin.PENNY).current_amount()

    assert actual == 1


def test_when_two_valid_coin_is_inserted_add_to_current_amount():
    vending_machine = VendingMachine()

    actual = (
        vending_machine.insert_coin(Coin.PENNY)
        .insert_coin(Coin.NICKEL)
        .current_amount()
    )

    assert actual == 6


# def test_when_a_valid_coint_is_inserted_display_will_be_updated():
