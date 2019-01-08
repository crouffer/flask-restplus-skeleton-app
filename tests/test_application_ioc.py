import pytest
from application.common.application_ioc import IApplicationIOC, ApplicationIOC


def test_constructor():
    uut = ApplicationIOC()
    assert isinstance(uut, ApplicationIOC)


def test_get_logger():
    uut = ApplicationIOC()
    logger = uut.get_logger()
    assert logger is not None


def test_get_logger_interface_not_implemented():
    class MyIoc(IApplicationIOC):
        def __init__(self):
            pass

    uut = MyIoc()
    assert uut is not None

    with pytest.raises(NotImplementedError):
        uut.get_logger()
