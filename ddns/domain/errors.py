"""Exception classes for the ddns application."""

class PublicIpResolverError(Exception):
    """An error resolving the public IP address."""

    def __init__(self, reason: str | None  = None):
        """Initialize a new PublicIpResolverError."""
        super().__init__(
            "Unable to resolve the public IP"
        )


class DynamicDnsUpdateError(Exception):
    """An error updating the dynamic DNS record."""

    def __init__(self, reason: str | None  = None):
        """Initialize a new PublicIpResolverError."""
        super().__init__(
            "Unable to update the dynamic DNS record"
        )


