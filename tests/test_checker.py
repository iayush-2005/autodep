from autodep.checker import get_missing_modules

def test_missing_modules():
    modules = ["os", "nonexistentmodule"]
    missing = get_missing_modules(modules)
    assert "nonexistentmodule" in missing
    assert "os" not in missing
