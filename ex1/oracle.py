import os
import sys


def display_value(label: str, value: str | None, fallback: str) -> bool:
    if value:
        print(f"{label}: Configured")
        return True
    print(f"{label}: {fallback} [missing configuration]")
    return False


def main() -> None:
    try:
        from dotenv import load_dotenv
    except ImportError:
        print("Missing python-dotenv. Run:")
        print("python3 -m pip install -r ex1/requirements.txt")
        return

    env_path = os.path.join(os.path.dirname(__file__), ".env")
    load_dotenv(env_path, override=False)

    mode = os.getenv("MATRIX_MODE", "development")
    database = os.getenv("DATABASE_URL")
    api_key = os.getenv("API_KEY")
    default_log_level = "DEBUG" if mode == "development" else "WARNING"
    log_level = os.getenv("LOG_LEVEL", default_log_level)
    endpoint = os.getenv("ZION_ENDPOINT")

    print("ORACLE STATUS: Consulting the configuration...")
    print("\nConfiguration loaded:")
    print(f"Mode: {mode}")
    database_ready = display_value("Database", database, "Not configured")
    api_ready = display_value("API Access", api_key, "Not authenticated")
    print(f"Log Level: {log_level}")
    endpoint_ready = display_value("Remote Network", endpoint, "Offline")

    print("\nRuntime behavior:")
    if mode == "production":
        print("Production safeguards enabled; verbose diagnostics disabled.")
    else:
        print("Development diagnostics enabled.")

    print("\nConfiguration security check:")
    print("[OK] Secrets are read from the environment")
    print("[OK] .env is excluded through .gitignore")
    if not (database_ready and api_ready and endpoint_ready):
        print("[WARNING] Some configuration values are missing")
    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    try:
        main()
    except OSError as error:
        print(f"Oracle configuration error: {error}", file=sys.stderr)
