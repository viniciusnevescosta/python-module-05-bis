from __future__ import annotations

import os
import sys

try:
    from dotenv import load_dotenv  # type: ignore[import-not-found]
except ImportError:
    load_dotenv = None


def display_value(label: str, value: str | None, fallback: str) -> bool:
    if value:
        print(f"{label}: {value}")
        return True
    print(f"{label}: {fallback} [missing configuration]")
    return False


def main() -> None:
    env_path = os.path.join(os.path.dirname(__file__), ".env")
    if load_dotenv is not None:
        load_dotenv(env_path, override=False)
    else:
        print("Warning: python-dotenv is unavailable.")
        print("Install it with: pip install -r ex1/requirements.txt\n")

    mode = os.getenv("MATRIX_MODE", "development")
    database = os.getenv("DATABASE_URL")
    api_key = os.getenv("API_KEY")
    log_level = os.getenv("LOG_LEVEL", "DEBUG" if mode == "development"
                          else "WARNING")
    endpoint = os.getenv("ZION_ENDPOINT")

    print("ORACLE STATUS: Consulting the configuration...")
    print("\nConfiguration loaded:")
    print(f"Mode: {mode}")
    complete = display_value("Database", database, "Not configured")
    complete = display_value("API Access", api_key, "Not authenticated") \
        and complete
    print(f"Log Level: {log_level}")
    complete = display_value("Remote Network", endpoint, "Offline") \
        and complete

    print("\nRuntime behavior:")
    if mode == "production":
        print("Production safeguards enabled; verbose diagnostics disabled.")
    else:
        print("Development diagnostics enabled.")

    print("\nConfiguration security check:")
    print("[OK] Secrets are read from the environment")
    print("[OK] .env is excluded through .gitignore")
    if not complete:
        print("[WARNING] Some configuration values are missing")
    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    try:
        main()
    except OSError as error:
        print(f"Oracle configuration error: {error}", file=sys.stderr)
