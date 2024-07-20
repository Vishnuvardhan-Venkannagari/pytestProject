import pytest

@pytest.mark.login
def testLogin():
    assert 1 == 1

@pytest.mark.Payments
def testPayment():
    assert 1 == 1
    
@pytest.mark.Payments    
def testAccess():
    assert 1 == 1

@pytest.mark.logout
def testLogout():
    assert 1 == 1