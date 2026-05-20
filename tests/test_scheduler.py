from __future__ import annotations

from datetime import UTC, datetime, timedelta

import pytest

from bot.scheduler import next_recurrence

NOW = datetime(2026, 5, 14, 12, 0, tzinfo=UTC)


class TestNextRecurrenceDaily:
    def test_one_day_ahead_when_due_yesterday(self):
        last = NOW - timedelta(hours=1)
        assert next_recurrence(NOW, last, "daily") == last + timedelta(days=1)

    def test_fast_forwards_past_missed_days(self):
        last = NOW - timedelta(days=10)
        result = next_recurrence(NOW, last, "daily")
        assert result > NOW
        # Result should be the first slot strictly after NOW.
        assert result - timedelta(days=1) <= NOW

    def test_already_in_future_advances_by_one_day(self):
        last = NOW + timedelta(hours=2)
        assert next_recurrence(NOW, last, "daily") == last + timedelta(days=1)


class TestNextRecurrenceWeekly:
    def test_advances_one_week(self):
        last = NOW - timedelta(hours=1)
        assert next_recurrence(NOW, last, "weekly") == last + timedelta(weeks=1)

    def test_fast_forwards_past_missed_weeks(self):
        last = NOW - timedelta(weeks=5)
        result = next_recurrence(NOW, last, "weekly")
        assert result > NOW
        assert result - timedelta(weeks=1) <= NOW


class TestNextRecurrenceInvalid:
    def test_unknown_recurrence_raises(self):
        with pytest.raises(KeyError):
            next_recurrence(NOW, NOW, "hourly")  # type: ignore[arg-type]
