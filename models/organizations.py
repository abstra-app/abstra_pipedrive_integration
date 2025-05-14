from dataclasses import dataclass
from typing import List, Dict, Optional
from datetime import datetime


@dataclass
class Organization:
    id: int
    name: Optional[str]
    owner_id: Optional[int]
    org_id: Optional[int]
    add_time: Optional[datetime]
    update_time: Optional[datetime]
    address: Optional[Dict]
    is_deleted: Optional[bool]
    visible_to: Optional[int]
    label_ids: Optional[List[int]]
    custom_fields: Optional[Dict]

    @staticmethod
    def from_dict(data: Dict) -> "Organization":
        """
        Create a Organization instance from a dictionary.
        """

        if "id" not in data:
            raise ValueError("Missing 'id' key in the data dictionary.")

        return Organization(
            id = data["id"],
            name = data.get("name", None),
            owner_id = data.get("owner_id", None),
            org_id = data.get("org_id", None),
            add_time = data.get("add_time", None),
            update_time = data.get("update_time", None),
            address = data.get("address", None),
            is_deleted = data.get("is_deleted", None),
            visible_to = data.get("visible_to", None),
            label_ids = data.get("label_ids", None),
            custom_fields = data.get("custom_fields", []),
        )

    def to_dict(self) -> Dict:
        """
        Convert the Organization instance to a dictionary.
        """
        return {
            "id": self.id,
            "name": self.name,
            "owner_id": self.owner_id,
            "org_id": self.org_id,
            "add_time": self.add_time,
            "update_time": self.update_time,
            "address": self.address,
            "is_deleted": self.is_deleted,
            "visible_to": self.visible_to,
            "label_ids": self.label_ids,
            "custom_fields": self.custom_fields,
        }
