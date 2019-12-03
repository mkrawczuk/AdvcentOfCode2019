class Parser:
    """ A 'default' parser, or rather the parser interface. """
    def parse(self, inputdata: str):
        raise NotImplementedError("No appropriate parser implemented.")

class NewlineParser(Parser):
    """ For newline-separated list of numbers. """
    def parse(self, inputdata: str):
        return list(map(int, inputdata.split()))

class CommaParser(Parser):
    """ For comma-separated list of numbers. """
    def parse(self, inputdata: str):
        return list(map(int, inputdata.split(',')))

class Day3Parser(Parser):
    """ For Day 3's special kind of input. """
    def parse(self, inputdata: str):
        return list(map(lambda x: x.split(','), inputdata.split()))

_parser_for_day = {
        1: NewlineParser,
        2: CommaParser,
        3: Day3Parser
        }

def ParserForDay(day: int):
    return _parser_for_day.get(day, Parser)()
