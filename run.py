import argparse
import sys
from pathlib import Path

from python_advanced_gists.metacls_singleton import main as metacls_main

# Добавить корень проекта в PYTHONPATH
project_root = Path(__file__).parent.resolve()
sys.path.insert(0, str(project_root))

def main():
    parser = argparse.ArgumentParser(description='Запуск модулей проекта')
    parser.add_argument(
        '--metacls_singleton',
        action='store_true',
        help='Запустить модуль metacls_singleton'
    )
    # todo Добавить следующие модули

    args = parser.parse_args()
    if args.metacls_singleton:
        print("Запуск metacls_singleton...")
        metacls_main()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
