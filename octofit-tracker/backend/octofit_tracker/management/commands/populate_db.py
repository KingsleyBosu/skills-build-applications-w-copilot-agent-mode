from django.core.management.base import BaseCommand
from octofit_app.models import User, Team, Activity, Leaderboard, Workout
from django.db import transaction
from datetime import timedelta

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activity, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        with transaction.atomic():
            # Clear existing data
            User.objects.all().delete()
            # Clear all relevant tables to avoid conflicts
            Team.objects.all().delete()
            Activity.objects.all().delete()
            Leaderboard.objects.all().delete()
            Workout.objects.all().delete()

            # Create users
            users = [
                User(username='thundergod', email='thundergod1@mhigh.edu', password='thundergodpassword'),
                User(username='metalgeek', email='metalgeek2@mhigh.edu', password='metalgeekpassword'),
                User(username='zerocool', email='zerocool3@mhigh.edu', password='zerocoolpassword'),
                User(username='crashoverride', email='crashoverride4@hmhigh.edu', password='crashoverridepassword'),
                User(username='sleeptoken', email='sleeptoken5@mhigh.edu', password='sleeptokenpassword'),
            ]
            # Save users individually to ensure their IDs are populated
            for user in users:
                user.save()

            # Remove redundant save calls for users
            # Save users to the database before associating them with teams
            # for user in users:
            #     user.save()

            # Create teams
            team1 = Team(name='Blue Team')
            team2 = Team(name='Gold Team')
            team1.save()
            team2.save()

            # Associate users with teams after saving
            team1.members.set(users)

            # Create activities
            activities = [
                Activity(user=users[0], activity_type='Cycling', duration=timedelta(hours=1)),
                Activity(user=users[1], activity_type='Crossfit', duration=timedelta(hours=2)),
                Activity(user=users[2], activity_type='Running', duration=timedelta(hours=1, minutes=30)),
                Activity(user=users[3], activity_type='Strength', duration=timedelta(minutes=30)),
                Activity(user=users[4], activity_type='Swimming', duration=timedelta(hours=1, minutes=15)),
            ]
            Activity.objects.bulk_create(activities)

            # Create leaderboard entries
            leaderboard_entries = [
                Leaderboard(user=users[0], score=100),
                Leaderboard(user=users[1], score=90),
                Leaderboard(user=users[2], score=95),
                Leaderboard(user=users[3], score=85),
                Leaderboard(user=users[4], score=80),
            ]
            Leaderboard.objects.bulk_create(leaderboard_entries)

            # Create workouts
            workouts = [
                Workout(name='Cycling Training', description='Training for a road cycling event'),
                Workout(name='Crossfit', description='Training for a crossfit competition'),
                Workout(name='Running Training', description='Training for a marathon'),
                Workout(name='Strength Training', description='Training for strength'),
                Workout(name='Swimming Training', description='Training for a swimming competition'),
            ]
            Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
