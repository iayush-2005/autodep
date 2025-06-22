from autodep.scanner import extract_imports_from_directory

def test_extract_imports(tmp_path):
    sample_file = tmp_path / "sample.py"
    sample_file.write_text("import os\nimport sys\n")
    imports = extract_imports_from_directory(str(tmp_path))
    assert set(imports) == {"os", "sys"}
