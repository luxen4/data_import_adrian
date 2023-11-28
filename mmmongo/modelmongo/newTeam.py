class NewTeam:
    def __init__(self, team_id, name, description, project_id):
        self.team_id=team_id
        self.name=name
        self.description=description
        self.project_id=project_id
    
    def __str__(self) -> str:
        return f"team_id:{self.team_id}, name:{self.name}, description:{self.description}, skill_id:{self.project_id}"
    def __repr__(self):
        return self.__str__()

        
      