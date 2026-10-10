from app import build_message


def test_build_message() -> None:
    text = build_message()
    assert "GitHub Achievement Lab" in text
    assert "GitHub" in text
