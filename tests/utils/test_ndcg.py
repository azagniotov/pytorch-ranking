from src.utils import ndcg

def test_true():
    assert True


def test_ndcg_true():
    s = ndcg.NDCG()
    assert s.true() is True


def test_ndcg_false():
    assert ndcg.NDCG.false() is False
