from flask import request
from flask_restful import Resource
from http import HTTPStatus
from models.schedule import Schedule, schedule_list


class ScheduleListResource(Resource):
    def get(self):
        data = []
        for schedule in schedule_list:
            if schedule.is_publish is True:
                data.append(schedule.data)

        return {'data': data}, HTTPStatus.OK

    def post(self):
        data = request.get_json()
        schedule = Schedule(name=data['name'],
                            weight=data['weight'],
                            height=data['height'],
                            description=data['description'],
                            breakfast=data['breakfast'],
                            lunch=data['lunch'],
                            dinner=data['dinner'],
                            desert=data['desert'])
        schedule_list.append(schedule)
        return schedule.data, HTTPStatus.CREATED


class ScheduleResource(Resource):
    def get(self, schedule_id):
        schedule = next(schedule for schedule in schedule_list if schedule.id == schedule_id and schedule.is_publish == True)

        if schedule is None:
            return {'message': 'schedule not found'}, HTTPStatus.NOT_FOUND

        return schedule.data, HTTPStatus.OK

    def put(self, schedule_id):
        data = request.get_json()
        schedule = next((schedule for schedule in schedule_list if schedule.id == schedule_id), None)

        if schedule is None:
            return {'message': 'schedule not found'}, HTTPStatus.NOT_FOUND

        schedule.name = data['name']
        schedule.weight = data['weight']
        schedule.height = data['height']
        schedule.description = data['description']
        schedule.breakfast = data['breakfast']
        schedule.lunch = data['lunch']
        schedule.dinner = data['dinner']
        schedule.desert = data['desert']

        return schedule.data.HTTPStatus.OK


class ScheduleResourceResource(Resource):
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
