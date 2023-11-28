class NewProject:
    def __init__(self, project_id, name, description,skill_id,location_id,company_id):
        self.project_id=project_id
        self.name=name
        self.description=description
        self.skill_id=skill_id
        self.location_id=location_id
        self.company_id=company_id
    
    def __str__(self) -> str:
        return f"project_id:{self.project_id}, name:{self.name}, description:{self.description}, skill_id:{self.skill_id}, location_id={self.location_id} company_id:{self.location_id} "
    def __repr__(self):
        return self.__str__()