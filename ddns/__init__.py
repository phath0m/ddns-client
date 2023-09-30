"""Dynamic DNS Client Package."""
from argparse import ArgumentParser

from ddns.adapters import IpifyIpResolver, NamecheapDynamicDnsClient
from ddns.domain import Application


def create_argument_parser() -> ArgumentParser:
    """Create the argument parser for the application."""
    parser = ArgumentParser()
    parser.add_argument(
        "-H", "--host",
        required=True,
        help="The DNS host that will be updated."
    )
    parser.add_argument(
        "-d", "--domain",
        required=True,
        help="The DNS domain that host resides on."
    )
    parser.add_argument(
        "-p", "--password",
        required=True,
        help="DDNS client Password",
    )
    return parser


def main() -> None:
    """Run the application."""
    parser = create_argument_parser()
    args = parser.parse_args()

    ip_resolver = IpifyIpResolver()
    ddns_client = NamecheapDynamicDnsClient(args.password)

    app = Application(
        domain_name=args.domain,
        host=args.host,
        ip_resolver=ip_resolver,
        ddns_client=ddns_client,
    )

    app.update_dns_record()


if __name__ == "__main__":
    main()