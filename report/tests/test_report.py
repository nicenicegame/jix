import unittest

from django.contrib.auth.models import User
from django.test import TestCase
# Create your tests here.
from django.urls import reverse
from django.utils import timezone

from report.models import Report
from events.tests.test_event import create_event


def report_and_create_event(report_type, detail):
    """Create and event and report that event."""
    user = User.objects.create_user(username='testuser', password='secret123456')
    event = create_event("Walking", "Walk in Jungle", "sport", user)
    reported_at = timezone.now()
    report1 = Report.objects.create(event=event, report_type=report_type, detail=detail, reported_at=reported_at)

    report1.save()
    return report1


def report_event(event, report_type, detail):
    """Report an event."""
    reported_at = timezone.now()
    report1 = Report.objects.create(event=event, report_type=report_type, detail=detail, reported_at=reported_at)

    report1.save()
    return report1


class EventReportsTest(TestCase):
    """Test for Report Views."""

    def setUp(self):
        """Create a super user to view report feed."""
        self.user = User.objects.create_superuser(
            username='foobar',
            email='foo@bar.com',
            password='barbaz')
        self.client.force_login(user=self.user)

    def test_no_reports(self):
        """If no reports exist, an appropriate message is displayed."""
        response = self.client.get(reverse('report:feed'))
        self.assertContains(response, "No reports.")
        self.assertEqual(response.status_code, 200)

    def test_report_category(self):
        """The report is show in according to category, when you choose category."""
        report = report_and_create_event("hate-speech", "Hi", )
        event1 = create_event("Dinner", "Eat KFC", "eating", user=self.user)
        report2 = report_event(event1, "spam", "S P A M", )
        url = reverse('report:report_by_category', args=(report.report_type,))
        response = self.client.get(url)
        self.assertContains(response, report.event)
        self.assertNotContains(response, report2.event)
        self.assertNotContains(response, "No reports in this category.")


if __name__ == '__main__':
    unittest.main(verbosity=2)
