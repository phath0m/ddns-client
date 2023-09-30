"""The application."""
from ddns.domain.ports import DynamicDnsClient, PublicIpResolver


class Application:
    """The application class."""

    def __init__(
        self,
        *,
        domain_name:    str,
        host:           str,
        ddns_client:    DynamicDnsClient,
        ip_resolver:    PublicIpResolver,
    ):
        """Initialize a new application."""
        self._domain_name = domain_name
        self._host = host
        self._ddns_client = ddns_client
        self._ip_resolver = ip_resolver

    def update_dns_record(self) -> None:
        """Update the dynamic record with our current public IP."""
        public_ip = self._ip_resolver.get_public_ip()
        self._ddns_client.update_dns_record(
            self._domain_name,
            self._host,
            public_ip,
        )