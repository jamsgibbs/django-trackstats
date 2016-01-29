import random
from datetime import date, timedelta, datetime, time

from django.test import TestCase
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.utils import timezone

from trackstats.models import Domain, Metric, Statistic, Period
from trackstats.trackers import CountObjectsByDateTracker

User = get_user_model()


class TrackersTestCase(TestCase):

    def setUp(self):
        self.users_domain = Domain.objects.register(ref='users')
        self.user_count = Metric.objects.register(
            domain=self.users_domain,
            ref='user_count')
        self.expected_signups = {}
        dt = date.today() - timedelta(days=7)
        signups_lifetime = 0
        while dt != date.today():
            signups_on_day = random.randint(1, 5)
            signups_lifetime += signups_on_day
            date_joined = timezone.make_aware(
                datetime.combine(
                    dt,
                    time()))
            self.expected_signups[dt] = {
                'lifetime': signups_lifetime,
                'day': signups_on_day
            }
            for i in range(signups_on_day):
                User.objects.create(
                    username='user{}_{}'.format(dt, i),
                    date_joined=date_joined)
            dt += timedelta(days=1)

    def test_count_lifetime(self):
        CountObjectsByDateTracker(
            period=Period.LIFETIME,
            metric=self.user_count,
            date_field='date_joined').track(User.objects.all())
        stats = Statistic.objects.narrow(
            metrics=[self.user_count],
            period=Period.LIFETIME)
        for stat in stats:
            self.assertEqual(
                stat.value,
                self.expected_signups[stat.date]['lifetime'])
        self.assertEqual(
            stats.count(),
            len(self.expected_signups))

    def test_count_daily(self):
        CountObjectsByDateTracker(
            period=Period.DAY,
            metric=self.user_count,
            date_field='date_joined').track(User.objects.all())
        stats = Statistic.objects.narrow(
            metrics=[self.user_count],
            period=Period.DAY)
        for stat in stats:
            self.assertEqual(
                stat.value,
                self.expected_signups[stat.date]['day'])
        self.assertEqual(
            stats.count(),
            len(self.expected_signups))
