import argparse

from .openai_utils import get_symbols, get_symbol

def main():
    parser = argparse.ArgumentParser(description='Get matching symbols for a prompt')
    parser.add_argument('prompt', type=str, help='The prompt to match symbols for')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--all', action='store_true', default=True, help='Ask for many symbols')
    group.add_argument('--one', action='store_true', help='Ask for one symbol')

    args = parser.parse_args()

    if args.all:
        symbols = get_symbols(args.prompt)
        print(symbols)
    elif args.one:
        symbol = get_symbol(args.prompt)
        print(symbol)

if __name__ == '__main__':
    main()