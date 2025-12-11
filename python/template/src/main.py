"""Main entry point for python project."""

from src.sub_folder_1.test1 import calculate
from src.sub_folder_2.test2 import double_calculate


def main():
    """Main application entry point."""
    try:
        result = calculate(2, 3)
        double_result = double_calculate(2, 3)
        print(f"calculate(2, 3) = {result}")
        print(f"double_calculate(2, 3) = {double_result}")

        print("Application started. Press Ctrl+C to exit.")
        while True:
            pass
    except KeyboardInterrupt:
        print("\n[shutdown] Received KeyboardInterrupt")
    except Exception as e:
        print(f"[ERROR] Startup error: {e}")
        raise


if __name__ == "__main__":
    main()
