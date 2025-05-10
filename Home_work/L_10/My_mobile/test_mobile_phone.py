from My_mobile import MobilePhone

def test_turn_on():
    phone = MobilePhone(375291234455)
    assert not phone.switch # Телефон выключен.
 
    message = phone.turn_on()
    assert phone.switch  # Телефон включен.
    assert message == 'mobile phone 375291234455 is turned on'

def test_call_when_off():
    phone = MobilePhone(375291112233)

    message = phone.call("291111122")
    assert message == "Mobile phone is turned off. Can't make a call."


def test_turn_off():
    phone = MobilePhone("375291112233")
    phone.turn_on()
    message = phone.turn_off()
    assert not phone.switch  # Телефон выключен.
    assert message == "mobile phone 375291112233 is turned off"

def test_call_when_on():
    phone = MobilePhone("375291112233")
    phone.turn_on()
    message = phone.call("291111122")
    assert message == "calling 291111122"
