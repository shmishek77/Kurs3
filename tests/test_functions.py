from src.functions import *


def test_date_format():
    assert date_format("2019-08-26T10:50:58.294041") == "26.08.2019"
    assert date_format("2018-11-08T08:21:45.902633") == "08.11.2018"
    assert date_format("2019-07-08T00:08:32.986663") == "08.07.2019"
    assert date_format("2019-09-06T00:48:01.081967") == "06.09.2019"
    assert date_format("2019-08-19T16:30:41.967497") == "19.08.2019"
    assert date_format("2018-12-22T02:02:49.564873") == "22.12.2018"
    assert date_format("2018-06-20T03:59:34.851630") == "20.06.2018"
    assert date_format("2019-04-18T11:22:18.800453") == "18.04.2019"


def test_from_():
    assert from_("Visa Platinum 8990922113665229") == "Visa Platinum 8990 92** **** 5229 ->"
    assert from_("Счет 72082042523231456215") == "Счет **6215 ->"
    assert from_("МИР 4878656375033856") == "МИР 4878 65** **** 3856 ->"
    assert from_("Maestro 3000704277834087") == "Maestro 3000 70** **** 4087 ->"
    assert from_("MasterCard 3595832182277400") == "MasterCard 3595 83** **** 7400 ->"
    assert from_("Visa Classic 4062745111784804") == "Visa Classic 4062 74** **** 4804 ->"
    assert from_("Visa Gold 3654412434951162") == "Visa Gold 3654 41** **** 1162 ->"
    assert from_("Счет 43475624104328495820") == "Счет **5820 ->"


def test_to():
    assert to("Счет 72731966109147704472") == "Счет **4472"
    assert to("МИР 9425591958944146") == "МИР 9425 59** **** 4146"
    assert to("MasterCard 3595832182277400") == "MasterCard 3595 83** **** 7400"
    assert to("Maestro 3000704277834087") == "Maestro 3000 70** **** 4087"
    assert to("Visa Platinum 8990922113665229") == "Visa Platinum 8990 92** **** 5229"
    assert to("Visa Classic 4062745111784804") == "Visa Classic 4062 74** **** 4804"
    assert to("Visa Gold 3654412434951162") == "Visa Gold 3654 41** **** 1162"
    assert to("Счет 43475624104328495820") == "Счет **5820"