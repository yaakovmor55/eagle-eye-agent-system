class Agent:
    def __init__(self, code_name, real_name,status, location, mission_completed, agent_id = None):
        self.id = agent_id
        self.code_name = code_name
        self.real_name = real_name
        self.status = status
        self.location = location
        self.mission_completed = mission_completed

    def __str__(self):
        return (
            f"[{self.id if self.id else '-'}]"
            f"Code Name: {self.code_name} | "
            f"Real Name: {self.real_name} | "
            f"Location: {self.location} | "
            f"Status: {self.status} | "
            f"Missions: {self.mission_completed}"
        )