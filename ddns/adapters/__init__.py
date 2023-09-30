"""Top-level module for the adapters package."""
from .ipify_ip_resolver import IpifyIpResolver
from .namecheap_ddns import NamecheapDynamicDnsClient

__all__ = ["IpifyIpResolver", "NamecheapDynamicDnsClient"]