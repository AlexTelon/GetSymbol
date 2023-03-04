import sys

from .openai_utils import get_symbols, get_symbol

def main():
    prompt = ' '.join(sys.argv[1:])
    if prompt == '':
        return
    print(get_symbols(prompt))
    # print(get_symbol(prompt))

if __name__ == '__main__':
    main()