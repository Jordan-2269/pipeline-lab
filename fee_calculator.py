def cancellation_fee(hours_before):
    """Return the cancellation fee in dollars."""
    if hours_before < 0:
        raise ValueError("hours_before cannot be negative")
    if hours_before >= 24:
        return 0
    return 25
