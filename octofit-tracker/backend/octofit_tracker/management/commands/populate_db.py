from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # 데이터 삭제
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # 팀 생성
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # 유저 생성
        users = [
            User.objects.create(email='ironman@marvel.com', name='Iron Man', team='Marvel'),
            User.objects.create(email='captain@marvel.com', name='Captain America', team='Marvel'),
            User.objects.create(email='batman@dc.com', name='Batman', team='DC'),
            User.objects.create(email='superman@dc.com', name='Superman', team='DC'),
        ]

        # 활동 생성
        Activity.objects.create(user='Iron Man', activity_type='Running', duration=30)
        Activity.objects.create(user='Captain America', activity_type='Cycling', duration=45)
        Activity.objects.create(user='Batman', activity_type='Swimming', duration=25)
        Activity.objects.create(user='Superman', activity_type='Running', duration=60)

        # 리더보드 생성
        Leaderboard.objects.create(user='Iron Man', score=100)
        Leaderboard.objects.create(user='Captain America', score=90)
        Leaderboard.objects.create(user='Batman', score=95)
        Leaderboard.objects.create(user='Superman', score=110)

        # 운동 생성
        Workout.objects.create(name='Push Ups', description='Do 20 push ups')
        Workout.objects.create(name='Sit Ups', description='Do 30 sit ups')
        Workout.objects.create(name='Squats', description='Do 40 squats')

        self.stdout.write(self.style.SUCCESS('octofit_db에 테스트 데이터가 성공적으로 추가되었습니다.'))
