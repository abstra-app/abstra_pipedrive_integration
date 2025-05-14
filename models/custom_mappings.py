from typing import Dict


class CustomMappings:
    """
    A mapping of custom field keys to their names.
    """

    _custom_field_mapping_deal: Dict[str, str]
    _custom_field_mapping_organization: Dict[str, str]
    _user_id_mapping: Dict[str, str]
    _stage_id_mapping: Dict[str, str]
    _pipeline_id_mapping: Dict[str, str]
    _channel_id_mapping: Dict[str, str]

    def __init__(
        self, 
        custom_field_mapping_deal: Dict[str, str],
        custom_field_mapping_organization: Dict[str, str],
        user_id_mapping: Dict[str, str],
        stage_id_mapping: Dict[str, str],
        pipeline_id_mapping: Dict[str, str],
        channel_id_mapping: Dict[str, str]
    ):

        self._custom_field_mapping_deal = custom_field_mapping_deal
        self._custom_field_mapping_organization = custom_field_mapping_organization
        self._user_id_mapping = user_id_mapping
        self._stage_id_mapping = stage_id_mapping
        self._pipeline_id_mapping = pipeline_id_mapping
        self._channel_id_mapping = channel_id_mapping

    def get_custom_field_mapping_deal(self, key: str, default: str) -> str:
        return self._custom_field_mapping_deal.get(str(key), default)

    def get_custom_field_mapping_organization(self, key: str, default: str) -> str:
        return self._custom_field_mapping_organization.get(str(key), default)

    def get_user_id_mapping(self, key: str, default: str) -> str:
            return self._user_id_mapping.get(str(key), default)

    def get_stage_id_mapping(self, key: str, default: str) -> str:
            return self._stage_id_mapping.get(str(key), default)

    def get_pipeline_id_mapping(self, key: str, default: str) -> str:
            return self._pipeline_id_mapping.get(str(key), default)

    def get_channel_id_mapping(self, key: str, default: str) -> str:
            return self._channel_id_mapping.get(str(key), default)


def get_custom_mappings(
    custom_field_mapping_deal: Dict[str, str],
    custom_field_mapping_organization: Dict[str, str],
    user_id_mapping: Dict[str, str],
    stage_id_mapping: Dict[str, str],
    pipeline_id_mapping: Dict[str, str],
    channel_id_mapping: Dict[str, str]
) -> CustomMappings:
    """
    Get the custom field mapping.
    """
    return CustomMappings(
        custom_field_mapping_deal,
        custom_field_mapping_organization,
        user_id_mapping,
        stage_id_mapping,
        pipeline_id_mapping,
        channel_id_mapping,
    )


