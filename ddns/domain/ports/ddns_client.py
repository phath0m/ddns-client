from abc import ABCMeta, abstractmethod

class DynamicDnsClient(metaclass=ABCMeta):
    """Client interface for interacting with a dynamic DNS service."""

    @abstractmethod
    def update_dns_record(
        self,
        domain_name:    str,
        host:           str,
        ip_address:     str,
    ) -> None:
        """Updates the host on ths specified domain name to the new IP."""
