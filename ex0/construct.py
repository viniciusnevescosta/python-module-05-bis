import os
import site
import sys


def inside_virtual_environment() -> bool:
    return sys.prefix != sys.base_prefix


def main() -> None:
    if inside_virtual_environment():
        print("LABORATORY STATUS: The laboratory is sealed\n")
        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environment: {os.path.basename(sys.prefix)}")
        print(f"Environment Path: {sys.prefix}")
        print("\nSUCCESS: You are working in an isolated environment!")
        print("Safe to install reagents without affecting the global system.")
        print("\nReagent installation path:")
        print(site.getsitepackages()[0])
    else:
        print("LABORATORY STATUS: You are working in the open\n")
        print(f"Current Python: {sys.executable}")
        print("Virtual Environment: None detected")
        print(f"Global package prefix: {sys.base_prefix}")
        print("\nWARNING: You are in the global environment!")
        print("Every reagent you install here leaks into the whole system.")
        print("\nTo seal the laboratory, run:")
        print("python3 -m venv lab_env")
        print("source lab_env/bin/activate # On Unix")
        print(r"lab_env\Scripts\activate # On Windows")
        print("\nThen run this program again.")


if __name__ == "__main__":
    main()
