from extensions import db

schedule_list = []


def get_by_id():
    if schedule_list:
        last_id = schedule_list[-1]
    else:
        return 1

    return last_id.id + 1


class Schedule(db.Model):
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
