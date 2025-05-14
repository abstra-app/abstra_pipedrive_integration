from dataclasses import dataclass
from typing import List, Dict, Optional
from datetime import datetime, date
from utils.time import (
    time_string_to_datetime,
    time_string_to_date,
)


@dataclass
class Lead:
    id: int
    title: Optional[str]
    owner_id: Optional[int]
    creator_id: Optional[int]
    label_ids: Optional[List[int]]
    person_id: Optional[int]
    organization_id: Optional[int]
    souce_name: Optional[str]
    origin: Optional[str]
    origin_id: Optional[str]
    channel: Optional[int]
    channel_id: Optional[str]
    is_archived: Optional[bool]
    was_seen: Optional[bool]
    value: Optional[Dict]
    expected_close_date: Optional[date]
    next_activity_id: Optional[int]
    add_time: Optional[datetime]
    update_time: Optional[datetime]
    visible_to: Optional[str]
    cc_email: Optional[str]

    @staticmethod
    def from_dict(data: Dict) -> "Lead":
        """
        Create a Activity instance from a dictionary.
        """

        if "id" not in data:
            raise ValueError("Missing 'id' key in the data dictionary.")

        return Lead(
            id=data["id"],
            title=data.get("title"),
            owner_id=data.get("owner_id"),
            creator_id=data.get("creator_id"),
            label_ids=data.get("label_ids"),
            person_id=data.get("person_id"),
            organization_id=data.get("organization_id"),
            souce_name=data.get("souce_name"),
            origin=data.get("origin"),
            origin_id=data.get("origin_id"),
            channel=data.get("channel"),
            channel_id=data.get("channel_id"),
            is_archived=data.get("is_archived"),
            was_seen=data.get("was_seen"),
            value=data.get("value"),
            expected_close_date=time_string_to_date(data.get("expected_close_date")),
            next_activity_id=data.get("next_activity_id"),
            add_time=time_string_to_datetime(data.get("add_time")),
            update_time=time_string_to_datetime(data.get("update_time")),
            visible_to=data.get("visible_to"),
            cc_email=data.get("cc_email"),
        )

    def to_dict(self) -> Dict:
        """
        Convert the Lead instance to a dictionary.
        """
        return {
            "id": self.id,
            "title": self.title,
            "owner_id": self.owner_id,
            "creator_id": self.creator_id,
            "label_ids": self.label_ids,
            "person_id": self.person_id,
            "organization_id": self.organization_id,
            "souce_name": self.souce_name,
            "origin": self.origin,
            "origin_id": self.origin_id,
            "channel": self.channel,
            "channel_id": self.channel_id,
            "is_archived": self.is_archived,
            "was_seen": self.was_seen,
            "value": self.value,
            "expected_close_date": self.expected_close_date,
            "next_activity_id": self.next_activity_id,
            "add_time": self.add_time.isoformat() if self.add_time else None,
            "update_time": self.update_time.isoformat() if self.update_time else None,
            "visible_to": self.visible_to,
            "cc_email": self.cc_email,
        }
