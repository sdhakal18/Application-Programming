from extensions import db

class Schedule(db.Model):

    def data(self):
        return {
            'id': self.id,
            'name': self.name,
            'weight': self.weight,
            'height': self.height,
            'description': self.description,
            'lunch': self.lunch,
            'dinner': self.lunch,
            'dessert = self.dessert'
            'user_id': self.user_id
        }

    @classmethod
    def get_all_published(cls):
        return cls.query.filter_by(is_publish=True).all()

    @classmethod
    def get_by_id(cls, recipe_id):
        return cls.query.filter_by(id=recipe_id).first()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    __tableName__ = 'diet plan'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    weight = db.Column(db.String)
    height = db.Column(db.String)
    description = db.Column(db.String)
    breakfast = db.Column(db.String)
    lunch = db.Column(db.String)
    dinner = db.Column(db.String)
    desert = db.Column(db.String)
    is_publish = db.Column(db.Boolean(), default=False)
    created_at = db.Column(db.DateTime(), nullable=False, server_default=db.func.now())
    updated_at = db.Column(db.DateTime(), nullable=False, server_default=db.func.now(), onupdate=db.func.now())

    user_id = db.Column(db.Integer(), db.ForeignKey("user.id"))
