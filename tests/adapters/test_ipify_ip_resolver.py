"""Test the Ipify adapter."""
from unittest.mock import Mock

import pytest

from ddns.adapters import IpifyIpResolver
from ddns.domain.errors import PublicIpResolverError


@pytest.fixture
def mock_get(mocker):
    """Mock the requests.get method."""
    mock = Mock()
    mocker.patch("requests.get", return_value=mock)
    return mock

def test_returns_public_ip(mock_get) -> None:
    """Test that the get_public_ip() method returns the public IP."""
    test_ip = "100.164.100.100"
    mock_get.status_code = 200
    mock_get.json.return_value = {"ip": test_ip}
    resolver = IpifyIpResolver()
    assert resolver.get_public_ip() == test_ip

def test_raises_public_ip_resolver_error(mock_get) -> None:
    """Test that the get_public_ip() method raises PublicIpResolverError."""
    test_ip = "100.164.100.100"
    mock_get.status_code = 400
    mock_get.json.return_value = {"ip": test_ip}
    resolver = IpifyIpResolver()

    with pytest.raises(PublicIpResolverError):
        resolver.get_public_ip()

