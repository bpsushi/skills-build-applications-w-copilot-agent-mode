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

        # Additional test data for users
        users.append({"email": "user3@example.com", "name": "User Three"})

        # Populate teams
        teams = [
            {"name": "Team Alpha", "members": ["user1@example.com", "user2@example.com"]},
        ]
        db.teams.insert_many(teams)

        # Additional test data for teams
        teams.append({"name": "Team Beta", "members": ["user3@example.com"]})

        # Populate activities
        activities = [
            {"user": "user1@example.com", "description": "Running", "timestamp": "2025-07-04T10:00:00Z"},
        ]
        db.activity.insert_many(activities)

        # Additional test data for activities
        activities.append({"user": "user3@example.com", "description": "Cycling", "timestamp": "2025-07-04T12:00:00Z"})

        # Populate leaderboard
        leaderboard = [
            {"user": "user1@example.com", "score": 100},
        ]
        db.leaderboard.insert_many(leaderboard)

        # Additional test data for leaderboard
        leaderboard.append({"user": "user3@example.com", "score": 80})

        # Populate workouts
        workouts = [
            {"user": "user1@example.com", "type": "Running", "duration": 30},
        ]
        db.workouts.insert_many(workouts)

        # Additional test data for workouts
        workouts.append({"user": "user3@example.com", "type": "Cycling", "duration": 45})

        self.stdout.write(self.style.SUCCESS('Successfully populated the database'))
