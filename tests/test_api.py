from pytest_testrail.plugin import pytestrail


@pytestrail.case("C1")
def test_api():
    result=True
    assert result


@pytestrail.case("C2")
def test_api_2():
    result = True
    assert result


@pytestrail.case("C3")
def test_api_3():
    result = True
    assert result


@pytestrail.case("C4")
def test_api_4():
    result = False
    assert result