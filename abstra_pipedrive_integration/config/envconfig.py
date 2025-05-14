import os
import dotenv


class EnvConfig:
    def __init__(self):
        pass

    @property
    def pipedrive_api_key(self):
        """
        Returns the Pipedrive API key from the environment variables.
        """

        dotenv.load_dotenv()
        return os.getenv("PIPEDRIVE_API_KEY")

    @property
    def company_domain(self):
        """
        Returns the company domain from the environment variables.
        """

        dotenv.load_dotenv()
        return os.getenv("COMPANY_DOMAIN")


def get_env_config():
    """
    Returns an instance of the EnvConfig class.
    """
    return EnvConfig()
