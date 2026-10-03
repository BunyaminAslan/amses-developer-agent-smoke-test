import pathlib


def test_readme_contains_intro():
    readme_path = pathlib.Path(__file__).resolve().parents[1] / "README.md"
    assert readme_path.exists(), "README.md must exist"
    text = readme_path.read_text(encoding="utf8")

    # Check for a short introduction about the Senior Developer Agent / OpenCode
    assert "Senior Developer Agent" in text, "README should mention 'Senior Developer Agent'"
    assert "OpenCode" in text, "README should mention 'OpenCode'"
    # Ensure a concise statement about approach is present
    assert "pragmatic" in text or "pragmatic," in text, "README should describe a pragmatic approach"
