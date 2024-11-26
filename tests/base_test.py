from src import app


def test_base():
    return 0


def test_run():
    assert app.runme() == 1
