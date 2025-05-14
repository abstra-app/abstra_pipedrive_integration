from interfaces.activity_interface import ActivityInterface
from interfaces.deal_interface import DealInterface
from interfaces.lead_interface import LeadInterface
from interfaces.organization_interface import OrganizationInterface

from config.envconfig import get_env_config

from pipedrive_api.pipedrive_api import PipedriveApi


class PipedriveSdk:
    deal_interface: DealInterface
    activity_interface: ActivityInterface
    lead_interface: LeadInterface
    organization_interface: OrganizationInterface

    def __init__(
        self,
        pipedrive_api: PipedriveApi,
    ):
        self.deal_interface = DealInterface(pipedrive_api)
        self.activity_interface = ActivityInterface(pipedrive_api)
        self.lead_interface = LeadInterface(pipedrive_api)
        self.organization_interface = OrganizationInterface(pipedrive_api)


def get_pipedrive_sdk() -> PipedriveSdk:
    """
    Instantiate and return a PipedriveSdk object.
    """

    envconfig = get_env_config()
    pipedrive_api = PipedriveApi(envconfig)
    return PipedriveSdk(pipedrive_api)
