"""Client for Namecheap's DDNS API."""
import requests

from ddns.domain.errors import DynamicDnsUpdateError
from ddns.domain.ports import DynamicDnsClient

HTTP_STATUS_OKAY = 200
NAMECHEAP_API_ENDPOINT = "https://dynamicdns.park-your-domain.com/update"


class NamecheapDynamicDnsClient(DynamicDnsClient):
    """Adapter for using Namecheap's dynamic DNS service."""

    def __init__(self, password: str) -> None:
        """Initialize a new NamecheapDynamicDnsClient instance."""
        self._password = password

    def update_dns_record(
        self,
        domain_name:    str,
        host:           str,
        ip_address:     str,
    ) -> None:
        """Update the host on the domain name to the new IP using Namecheap."""
        response = requests.post(NAMECHEAP_API_ENDPOINT, json={
            "host":     host,
            "domain":   domain_name,
            "ip":       ip_address,
            "password": self._password
        })

        if response.status_code != HTTP_STATUS_OKAY:
            raise DynamicDnsUpdateError