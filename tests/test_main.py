from app.main import health_check
from app.main import get_version

def test_health_check():
    result = health_check()

    assert result["status"] == "healthy"
    assert result["service"] == "cicd-lab"

def test_get_version():
    assert get_version() == "1.0.0"

# failed test

'''def test_intentional_failure():
    assert 1 == 2    '''