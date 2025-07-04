from django.core.management.base import BaseCommand
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        client = MongoClient("mongodb://localhost:27017/")
        db = client["octofit_db"]

        # Populate users
        users = [
            {"email": "user1@example.com", "name": "User One"},
            {"email": "user2@example.com", "name": "User Two"},
        ]
        db.users.insert_many(users)

        # Populate teams
        teams = [
            {"name": "Team Alpha", "members": ["user1@example.com", "user2@example.com"]},
        ]
        db.teams.insert_many(teams)

        # Populate activities
        activities = [
            {"user": "user1@example.com", "description": "Running", "timestamp": "2025-07-04T10:00:00Z"},
        ]
        db.activity.insert_many(activities)

        # Populate leaderboard
        leaderboard = [
            {"user": "user1@example.com", "score": 100},
        ]
        db.leaderboard.insert_many(leaderboard)

        # Populate workouts
        workouts = [
            {"user": "user1@example.com", "type": "Running", "duration": 30},
        ]
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database'))
