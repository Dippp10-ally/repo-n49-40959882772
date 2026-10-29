"""Simple retry helper."""


def retry_once(fn):
    """Retry a callback once after a failure."""

    def wrapped(*args, **kwargs):
        try:
            return fn(*args, **kwargs)
        except Exception:
            return fn(*args, **kwargs)

    return wrapped
