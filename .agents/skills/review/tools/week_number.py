#!/usr/bin/env python3
"""
Week number utility for review naming.

Usage:
    python week_number.py                    # Current week
    python week_number.py 2026-01-24         # Specific date
    python week_number.py --friday           # Friday of current week
    python week_number.py 2026-01-24 --friday # Friday of that week

Output format: WXX (e.g., W04)
"""

import sys
from datetime import datetime, timedelta


def get_week_number(date: datetime) -> int:
    """Get ISO week number for a date."""
    return date.isocalendar()[1]


def get_friday_of_week(date: datetime) -> datetime:
    """Get the Friday of the week containing the given date."""
    # weekday(): Monday=0, Friday=4
    days_until_friday = (4 - date.weekday()) % 7
    if date.weekday() > 4:  # Saturday or Sunday
        days_until_friday -= 7
    return date + timedelta(days=days_until_friday)


def format_week_number(week_num: int) -> str:
    """Format week number as W01, W02, etc."""
    return f"W{week_num:02d}"


def get_review_filename(date: datetime) -> str:
    """Generate the review filename with week number.

    Format: YYYY-MM-DD_WXX_week-review.md
    Uses the Friday of the review week.
    """
    friday = get_friday_of_week(date)
    week_num = get_week_number(friday)
    return f"{friday.strftime('%Y-%m-%d')}_W{week_num:02d}_week-review.md"


def get_review_title(date: datetime) -> str:
    """Generate the review title with week number.

    Format: Weekly Review — W04 (Week of 2026-01-24)
    """
    friday = get_friday_of_week(date)
    week_num = get_week_number(friday)
    return f"Weekly Review — W{week_num:02d} (Week of {friday.strftime('%Y-%m-%d')})"


def main():
    # Parse arguments
    date_str = None
    get_friday = False

    for arg in sys.argv[1:]:
        if arg == "--friday":
            get_friday = True
        elif arg == "--filename":
            # Output filename format
            date = datetime.now() if not date_str else datetime.strptime(date_str, "%Y-%m-%d")
            print(get_review_filename(date))
            return
        elif arg == "--title":
            # Output title format
            date = datetime.now() if not date_str else datetime.strptime(date_str, "%Y-%m-%d")
            print(get_review_title(date))
            return
        else:
            date_str = arg

    # Parse date or use today
    if date_str:
        try:
            date = datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            print(f"Error: Invalid date format '{date_str}'. Use YYYY-MM-DD.", file=sys.stderr)
            sys.exit(1)
    else:
        date = datetime.now()

    # Get Friday if requested
    if get_friday:
        date = get_friday_of_week(date)
        print(f"{date.strftime('%Y-%m-%d')} {format_week_number(get_week_number(date))}")
    else:
        print(format_week_number(get_week_number(date)))


if __name__ == "__main__":
    main()
