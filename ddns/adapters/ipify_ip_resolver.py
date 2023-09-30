"""Client for the ipify public IP resolver API."""
import requests

from ddns.domain.errors import PublicIpResolverError
from ddns.domain.ports import PublicIpResolver

HTTP_STATUS_OKAY = 200
IPIFY_API_ENDPOINT = "https://api.ipify.org"


class IpifyIpResolver(PublicIpResolver):
    """Adapter for using the Ipify public IP resolver API."""

    def get_public_ip(self) -> str:
        """Return the client's public IP via the ipify API."""
        response = requests.get(IPIFY_API_ENDPOINT, params={
            "format": "json"
        })

        if response.status_code != HTTP_STATUS_OKAY:
            raise PublicIpResolverError            

        return response.json()["ip"]