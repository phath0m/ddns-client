from abc import ABCMeta, abstractmethod

class PublicIpResolver(metaclass=ABCMeta):

    @abstractmethod
    def get_public_ip(self) -> str:
        """Retrieve the public IP address of this host"""