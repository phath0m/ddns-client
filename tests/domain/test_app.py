"""Test the Ipify adapter."""
from unittest.mock import Mock

from ddns.domain import Application


def test_update_dns_record() -> None:
    """Test that update_dns_record() correctly calls the DDNS adapter."""
    test_host = "host"
    test_domain = "website.com"
    test_ip = "1.1.1.1"

    mock_ddns_client = Mock()
    mock_public_ip_resolver = Mock()
    mock_public_ip_resolver.get_public_ip.return_value = test_ip

    app = Application(
        domain_name=test_domain,
        host=test_host,
        ddns_client=mock_ddns_client,
        ip_resolver=mock_public_ip_resolver
    )

    app.update_dns_record()

    mock_ddns_client.update_dns_record.assert_called_once_with(
        test_domain,
        test_host,
        test_ip,
    )