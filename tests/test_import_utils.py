from autodep.import_utils import filter_and_normalize_imports

def test_filter_and_normalize():
    raw = ["os", "sys", "numpy.linalg", "collections.defaultdict"]
    cleaned = filter_and_normalize_imports(raw)
    assert set(cleaned) == {"os", "sys", "numpy", "collections"}
