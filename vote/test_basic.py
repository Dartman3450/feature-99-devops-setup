def test_placeholder_pass():
    """Test sederhana yang akan selalu lulus (pass) untuk memverifikasi CI."""
    expected_value = 1
    actual_value = 1
    # Memastikan nilai 1 sama dengan 1
    assert actual_value == expected_value
    
def test_app_is_imported():
    """Memastikan bahwa modul utama (app.py) dapat diimpor tanpa error."""
    try:
        from app import app
        assert app is not None
    except ImportError:
        assert False, "Gagal mengimpor Flask App. Pastikan semua dependencies terinstal."
