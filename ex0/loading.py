import importlib


def check_reagent(name: str, purpose: str) -> bool:
    try:
        reagent = importlib.import_module(name)
    except ImportError:
        print(f"[MISSING] {name} - {purpose}")
        return False
    version = getattr(reagent, "__version__", "unknown")
    print(f"[OK] {name} ({version}) - {purpose}")
    return True


def main() -> None:
    print("REAGENT STATUS: Loading reagents...")
    print("\nChecking dependencies:\n")
    pandas_ready = check_reagent("pandas", "Data manipulation ready")
    numpy_ready = check_reagent("numpy", "Numerical computation ready")
    print("\npip vs Poetry:")
    print(
        "  requirements.txt declares what to install; pip resolves it "
        "at install time."
    )
    print(
        "  pyproject.toml declares the same constraints, and Poetry pins "
        "resolved versions"
    )
    print("  in poetry.lock so every install is identical.")
    if pandas_ready and numpy_ready:
        print("\nAll reagents present and accounted for.")
    else:
        print("\nInstall missing reagents with either:")
        print("pip install -r ex0/requirements.txt")
        print("poetry install")


if __name__ == "__main__":
    main()
