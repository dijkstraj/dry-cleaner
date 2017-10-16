from sys import argv

from PIL import Image
import glob
from os import path
import colorsys
from antlr4 import *
from CodeLexer import CodeLexer
from CodeParser import CodeParser
from CodeListener import CodeListener


class TokenCollector(CodeListener):
    def __init__(self):
        self.tokens = list()

    def exitToken(self, ctx):
        self.tokens.append(ctx.getText())


def token_color(max_length, token):
    intensity = 155 + (len(token) * 100 / max_length)
    if token[0] == "'":
        return intensity, 100, 100
    else:
        return 100, 100, intensity


def render_file_sim(filename):
    print path.basename(filename)

    input = FileStream(filename, 'utf-8')
    lexer = CodeLexer(input)
    tokens = CommonTokenStream(lexer)
    parser = CodeParser(tokens)
    tree = parser.code()
    walker = ParseTreeWalker()
    token_collector = TokenCollector()
    walker.walk(token_collector, tree)
    tokens = token_collector.tokens

    unique_tokens = list(set(tokens))
    token_hues = {unique_tokens[i]: float(i) / len(unique_tokens) for i in range(len(unique_tokens))}

    image = Image.new('RGB', (len(tokens), len(tokens)), (0, 0, 0))
    pixels = image.load()

    for i in range(len(tokens)):
        for j in range(len(tokens)):
            if tokens[i] == tokens[j]:
                pixels[i, j] = tuple(int(i * 255) for i in colorsys.hsv_to_rgb(token_hues[tokens[i]], 1, 1))

    image.save(path.basename(filename) + '.png', 'PNG')


def process_files(fileglob):
    for filename in glob.iglob(fileglob):
        render_file_sim(filename)


def main(argv):
    process_files(argv[1])


if __name__ == '__main__':
    main(argv)
