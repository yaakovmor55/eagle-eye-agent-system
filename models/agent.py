from  enum import  Enum

class Status(Enum):
    ACTIVE = "Active"
    INJURED = "Injured"
    MISSING = "Missing"
    RETIRED = "Retired"


class Agent:
    def __init__(self, code_name, real_name,status: Status.ACTIVE, location, missions_completed, agent_id = None):
        self.id = agent_id
        self.code_name = code_name
        self.real_name = real_name
        self.location = location
        self.status = status
        self.missions_completed = missions_completed

    def __str__(self):
        return (
            f"[{self.id if self.id else '-'}]"
            f"Code Name: {self.code_name} | "
            f"Real Name: {self.real_name} | "
            f"Location: {self.location} | "
            f"Status: {self.status.value} | "
            f"Missions: {self.missions_completed}"
        )