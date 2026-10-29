from src.retry_utils import retry_once


def test_retry_once_recovers_after_failure():
    calls = {"count": 0}

    @retry_once
    def flaky():
        calls["count"] += 1
        if calls["count"] == 1:
            raise RuntimeError("temporary fault")
        return "ok"

    assert flaky() == "ok"
