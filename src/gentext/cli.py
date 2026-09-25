import argparse
import sys


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="gentext")
    parser.add_argument("--version", action="store_true")
    args = parser.parse_args(argv)
    if args.version:
        from importlib.metadata import version

        print(version("gentext"))
        return 0
    parser.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
