from jokes import get_joke


def test_jokes():
    joke = get_joke()
    assert False
    assert "preambula" in joke
    assert "punchline" in joke
