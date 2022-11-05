import domino
import parser

sets = parser.parse_input(input())
for i in sets:
    domino.run(i)