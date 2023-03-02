import sys

from .openai_utils import get_chars

def main():
    prompt = ' '.join(sys.argv[1:])
    if prompt == '':
        return
    print(get_chars(prompt))

if __name__ == '__main__':
    main()