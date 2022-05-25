from panflute import *
from sys import stderr


headers = []


def same_headers(el, doc):
    if isinstance(el, Header):
        text = stringify(el)
        if text in headers:
            print("Одинаковые заголовки: " + text, file=stderr)
        else:
            headers.append(text)


def up_level(el, doc):
    if isinstance(el, Header) and el.level > 2:
        return Header(Str(stringify(el).upper()), level=el.level)


def bold(doc):
    doc.replace_keyword("BOLD", Strong(Str("BOLD")))


if __name__ == "__main__":
    run_filters([same_headers, up_level], prepare=bold)
