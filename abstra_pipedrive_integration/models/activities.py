from dataclasses import dataclass
from typing import List, Dict, Optional
from datetime import datetime, date, time
from utils.time import (
    time_string_to_datetime,
    time_string_to_date,
    time_string_to_time,
)


@dataclass
class Activity:
    id: int
    subject: Optional[str]
    type: Optional[str]
    owner_id: Optional[int]
    is_deleted: Optional[bool]
    add_time: Optional[datetime]
    update_time: Optional[datetime]
    deal_id: Optional[int]
    lead_id: Optional[str]
    person_id: Optional[int]
    org_id: Optional[int]
    project_id: Optional[str]
    due_date: Optional[date]
    due_time: Optional[time]
    duration: Optional[time]
    done: Optional[bool]
    busy: Optional[bool]
    marked_as_done_time: Optional[datetime]
    location: Optional[str]
    participants: Optional[List[Dict]]
    conference_meeting_client: Optional[str]
    conference_meeting_url: Optional[str]
    conference_meeting_id: Optional[str]
    public_description: Optional[str]
    priority: Optional[str]
    note: Optional[str]

    @staticmethod
    def from_dict(data: Dict) -> "Activity":
        """
        Create a Activity instance from a dictionary.
        """

        if "id" not in data:
            raise ValueError("Missing 'id' key in the data dictionary.")

        return Activity(
            id=data["id"],
            subject=data.get("subject"),
            type=data.get("type"),
            owner_id=data.get("owner_id"),
            is_deleted=data.get("is_deleted"),
            add_time=time_string_to_datetime(data.get("add_time")),
            update_time=time_string_to_datetime(data.get("update_time")),
            deal_id=data.get("deal_id"),
            lead_id=data.get("lead_id"),
            person_id=data.get("person_id"),
            org_id=data.get("org_id"),
            project_id=data.get("project_id"),
            due_date=time_string_to_date(data.get("due_date")),
            due_time=time_string_to_time(data.get("due_time")),
            duration=time_string_to_time(data.get("duration")),
            done=data.get("done"),
            busy=data.get("busy"),
            marked_as_done_time=time_string_to_datetime(
                data.get("marked_as_done_time")
            ),
            location=data.get("location"),
            participants=data.get("participants"),
            conference_meeting_client=data.get("conference_meeting_client"),
            conference_meeting_url=data.get("conference_meeting_url"),
            conference_meeting_id=data.get("conference_meeting_id"),
            public_description=data.get("public_description"),
            priority=data.get("priority"),
            note=data.get("note"),
        )

    def to_dict(self) -> Dict:
        """
        Convert the Activity instance to a dictionary.
        """
        return {
            "id": self.id,
            "subject": self.subject,
            "type": self.type,
            "owner_id": self.owner_id,
            "is_deleted": self.is_deleted,
            "add_time": self.add_time,
            "update_time": self.update_time,
            "deal_id": self.deal_id,
            "lead_id": self.lead_id,
            "person_id": self.person_id,
            "org_id": self.org_id,
            "project_id": self.project_id,
            "due_date": self.due_date,
            "due_time": self.due_time,
            "duration": self.duration,
            "done": self.done,
            "busy": self.busy,
            "marked_as_done_time": self.marked_as_done_time,
            "location": self.location,
            "participants": self.participants,
            "conference_meeting_client": self.conference_meeting_client,
            "conference_meeting_url": self.conference_meeting_url,
            "conference_meeting_id": self.conference_meeting_id,
            "public_description": self.public_description,
            "priority": self.priority,
            "note": self.note,
        }
