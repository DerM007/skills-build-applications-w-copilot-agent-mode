from bson import ObjectId
from datetime import timedelta

test_users = [
    {
        "_id": ObjectId(),
        "username": "student1",
        "email": "student1@example.com",
        "password": "password1",
    },
    {
        "_id": ObjectId(),
        "username": "student2",
        "email": "student2@example.com",
        "password": "password2",
    },
    {
        "_id": ObjectId(),
        "username": "student3",
        "email": "student3@example.com",
        "password": "password3",
    },
]

test_teams = [
    {
        "_id": ObjectId(),
        "name": "Team A",
        "members": [],
    }
]

test_activities = [
    {
        "_id": ObjectId(),
        "user": None,  # To be linked to a user
        "activity_type": "Running",
        "duration": timedelta(minutes=30),
    },
    {
        "_id": ObjectId(),
        "user": None,  # To be linked to a user
        "activity_type": "Cycling",
        "duration": timedelta(minutes=45),
    },
    {
        "_id": ObjectId(),
        "user": None,  # To be linked to a user
        "activity_type": "Swimming",
        "duration": timedelta(minutes=60),
    },
]

test_leaderboard = [
    {
        "_id": ObjectId(),
        "user": None,  # To be linked to a user
        "score": 100,
    },
    {
        "_id": ObjectId(),
        "user": None,  # To be linked to a user
        "score": 90,
    },
    {
        "_id": ObjectId(),
        "user": None,  # To be linked to a user
        "score": 80,
    },
]

test_workouts = [
    {
        "_id": ObjectId(),
        "name": "Morning Run",
        "description": "A 5km run to start the day",
    },
    {
        "_id": ObjectId(),
        "name": "Evening Swim",
        "description": "A relaxing swim session",
    },
]