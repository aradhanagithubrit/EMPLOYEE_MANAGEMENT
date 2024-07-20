from . import db

class Employee(db.mode):
    id = db.Column(db.Intege, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    position = db.Column(db.String(128),nullable=False)
    department = db.Column(db.String(128),nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "position": self.position,
            "department": self.department
        }
