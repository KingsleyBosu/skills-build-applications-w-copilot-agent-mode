from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(username="testuser", email="testuser@example.com", password="password123")

    def test_user_creation(self):
        user = User.objects.get(username="testuser")
        self.assertEqual(user.email, "testuser@example.com")

class TeamTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(username="teamuser", email="teamuser@example.com", password="password123")
        Team.objects.create(name="Test Team", members=[user])

    def test_team_creation(self):
        team = Team.objects.get(name="Test Team")
        self.assertEqual(team.name, "Test Team")

class ActivityTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(username="activityuser", email="activityuser@example.com", password="password123")
        Activity.objects.create(user=user, activity_type="Running", duration="00:30:00")

    def test_activity_creation(self):
        activity = Activity.objects.get(activity_type="Running")
        self.assertEqual(activity.duration, "00:30:00")

class LeaderboardTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(username="leaderboarduser", email="leaderboarduser@example.com", password="password123")
        Leaderboard.objects.create(user=user, score=100)

    def test_leaderboard_creation(self):
        leaderboard = Leaderboard.objects.get(score=100)
        self.assertEqual(leaderboard.user.username, "leaderboarduser")

class WorkoutTestCase(TestCase):
    def setUp(self):
        Workout.objects.create(name="Morning Yoga", description="A relaxing morning yoga session.")

    def test_workout_creation(self):
        workout = Workout.objects.get(name="Morning Yoga")
        self.assertEqual(workout.description, "A relaxing morning yoga session.")
