
class Incident:
    def __init__(self,id,
                title,
                type,
                severity,
                status,
                reporter,
                description):
        self.id=id
        self.title=title
        self.type=type
        self.severity=severity
        self.status=status
        self.reporter=reporter
        self.description=description
    def to_dict(self):
        return {"id": self.id,
                "title":self.title ,
                "type":self.type,
                "severity":self.severity,
                "status":self.status,
                "reporter":self.reporter,
                "description":self.description
                }
    
