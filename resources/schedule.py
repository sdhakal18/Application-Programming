from flask import request
from flask_restful import Resource
from http import HTTPStatus

from models.schedule import Schedule
from flask_jwt_extended import get_jwt_identity, jwt_required, jwt_optional


class ScheduleListResource(Resource):

    def get(self):
        schedules = Schedule.get_all_published()

        data = []

        for schedule in schedules:
            data.append(schedule.data())

            data.append(schedule.data)

        return {'data': data}, HTTPStatus.OK


@jwt_required
def post(self):
    json_data = request.get_json()
    current_user = get_jwt_identity()

    schedule = Schedule(name=json_data['name'],
                        weight=json_data['weight'],
                        height=json_data['height'],
                        description=json_data['description'],
                        breakfast=json_data['breakfast'],
                        lunch=json_data['lunch'],
                        dinner=json_data['dinner'],
                        desert=json_data['desert'],
                        user_id=current_user)
    schedule.save()
    return schedule.data(), HTTPStatus.CREATED


class ScheduleResource(Resource):
    @jwt_optional
    def get(self, schedule_id):
        schedule = Schedule.get_by_id(schedule_id == schedule_id)

        if schedule is None:
            return {'message': 'schedule not found'}, HTTPStatus.NOT_FOUND
        current_user = get_jwt_identity()
        if schedule.is_publish == False and schedule_id.user_id != current_user:
            return {'message': 'Access is not allowed'}, HTTPStatus.FORBIDDEN
        return schedule.data(), HTTPStatus.OK

    @jwt_required
    def put(self, schedule_id):
        json_data = request.get_json()
        schedule = Schedule.get_by_id(schedule_id == schedule_id)

        if schedule is None:
            return {'message': 'schedule not found'}, HTTPStatus.NOT_FOUND

        current_user = get_jwt_identity()
        if current_user != schedule.user_id:
            return {'message': 'Access is not allowed'}, HTTPStatus.FORBIDDEN

        schedule.name = json_data['name']
        schedule.weight = json_data['weight']
        schedule.height = json_data['height']
        schedule.description = json_data['description']
        schedule.breakfast = json_data['breakfast']
        schedule.lunch = json_data['lunch']
        schedule.dinner = json_data['dinner']
        schedule.desert = json_data['desert']

        schedule.save()

        return schedule.data.HTTPStatus.OK

    @jwt_required
    def delete(self, schedule_id):
        schedule = Schedule.get_by_id(schedule_id == schedule_id)

        if schedule is None:
            return {'message': 'schedule not found'}, HTTPStatus.NOT_FOUND

        current_user = get_jwt_identity()

        if current_user != recipe.user_id:
            return {'message': 'Access is not allowed'}, HTTPStatus.FORBIDDEN
        schedule.delete()
        return {}, HTTPStatus.NO_CONTENT


class SchedulePublishResource(Resource):
    def put(self, schedule_id):
        schedule = next((schedule for schedule in schedule_list if schedule.id == schedule_id), None)

        if schedule is None:
            return {'message': 'schedule not found'}, HTTPStatus.NOT_FOUND

        schedule.is_publish = True

        return {}, HTTPStatus.NO_CONTENT

    def delete(self, schedule_id):
        schedule = next((schedule for schedule in schedule_list if schedule.id == schedule_id), None)
        if schedule is None:
            return {'message': 'schedule not found'}, HTTPStatus.NOT_FOUND
        schedule.is_publish = False

        return {}, HTTPStatus.NO_CONTENT
