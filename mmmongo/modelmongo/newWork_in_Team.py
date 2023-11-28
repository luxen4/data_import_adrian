class NewWorks_in_Team:
    def __init__(self, person_id, team_id, role):
        self.person_id=person_id
        self.team_id=team_id
        self.role=role
        
    
    def __str__(self) -> str:
        return f"person_id:{self.person_id}, name:{self.team_id}, role:{self.role}"
    def __repr__(self):
        return self.__str__()
