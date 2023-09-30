"""Test the Ipify adapter."""
from unittest.mock import Mock

import pytest

from ddns.adapters import NamecheapDynamicDnsClient
from ddns.domain.errors import DynamicDnsUpdateError

NAMECHEAP_API_ENDPOINT = "https://dynamicdns.park-your-domain.com/update"

@pytest.fixture
def mock_post(mocker) -> Mock:
    """Mock the requests.get method."""
    mock = Mock()
    mocker.patch("requests.post", mock)
    return mock

def test_update_ddns_post_request(mock_post: Mock):
    """Test that update_dns_record() POSTs the correct request to the Namecheap API."""
    test_host = "host"
    test_domain = "website.com"
    test_password = "password"
    test_ip = "1.1.1.1"
    mock_post.return_value.status_code = 200
    ddns_client = NamecheapDynamicDnsClient(test_password)
    ddns_client.update_dns_record(test_domain, test_host, test_ip)

    expected_request = {
        "host":     test_host,
        "domain":   test_domain,
        "ip":       test_ip,
        "password": test_password,
    }

    mock_post.assert_called_once_with(NAMECHEAP_API_ENDPOINT, json=expected_request)

def test_update_ddns_raises_dynamic_dns_update_error(mock_post: Mock):
    """Test that update_dns_record() POSTs the correct request to the Namecheap API."""
    test_host = "host"
    test_domain = "website.com"
    test_password = "password"
    test_ip = "1.1.1.1"
    mock_post.return_value.status_code = 400
    ddns_client = NamecheapDynamicDnsClient(test_password)

    with pytest.raises(DynamicDnsUpdateError):
        ddns_client.update_dns_record(test_domain, test_host, test_ip)


