import csv
from collections import OrderedDict

def convert(data):
    human_readable = []
    for d in data:
        tmp = OrderedDict()

        tmp["Family"] = d.get("family")
        tmp["Description"] = d.get("description")
        tmp["Character"] = d.get("character")
        tmp["cell 1"] = ""
        tmp["cell 2"] = ""
        tmp["cell 3"] = ""
        tmp["Readable Braille"] = ""


        readable_braille = ""
        bump_set = d.get("braille")
        cell_number = 1
        for bump_cell in bump_set:

            braille_chars = ""
            readable_braille = readable_braille + " cell " + str(cell_number) + " contains"

            i = 0
            new_line_counter = 0
            while i < len(bump_cell):
                if bump_cell[i] == 0:
                    braille_chars = braille_chars + "•"

                if bump_cell[i] == 1:
                    readable_braille = readable_braille + " dot " + str(i + 1)
                    braille_chars = braille_chars + "●"

                i += 1
                new_line_counter += 1
                if new_line_counter == 2:
                    braille_chars = braille_chars + "\r"
                    new_line_counter = 0

            braille_chars = braille_chars.replace("••", "•  •")
            braille_chars = braille_chars.replace("●•", "● •")
            braille_chars = braille_chars.replace("•●", "• ●")
            braille_chars = braille_chars.replace("●●", "● ●")

            tmp["cell " + str(cell_number)] = braille_chars
            cell_number += 1


        tmp["Readable Braille"] = readable_braille
        human_readable.append(tmp)

    return human_readable




def main():
    data = [
  {
    "character": "not applicable",
    "description": "numeric",
    "family": "indicators",
    "braille": [
      [
        0,
        0,
        1,
        1,
        1,
        1
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "letter",
    "family": "indicators",
    "braille": [
      [
        0,
        0,
        0,
        0,
        0,
        1
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "word",
    "family": "indicators",
    "braille": [
      [
        0,
        0,
        0,
        0,
        0,
        1
      ],
      [
        0,
        0,
        0,
        0,
        0,
        1
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "passage",
    "family": "indicators",
    "braille": [
      [
        0,
        0,
        0,
        0,
        0,
        1
      ],
      [
        0,
        0,
        0,
        0,
        0,
        1
      ],
      [
        0,
        0,
        0,
        0,
        0,
        1
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "capital terminator",
    "family": "indicators",
    "braille": [
      [
        0,
        0,
        0,
        0,
        0,
        1
      ],
      [
        0,
        0,
        0,
        0,
        1,
        0
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "symbol",
    "family": "indicators",
    "braille": [
      [
        0,
        0,
        0,
        0,
        1,
        1
      ],
      [
        0,
        0,
        0,
        0,
        0,
        0
      ],
      [
        0,
        0,
        0,
        0,
        0,
        0
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "word",
    "family": "indicators",
    "braille": [
      [
        0,
        0,
        0,
        0,
        1,
        1
      ],
      [
        0,
        0,
        0,
        0,
        1,
        1
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "passage",
    "family": "indicators",
    "braille": [
      [
        0,
        0,
        0,
        0,
        1,
        1
      ],
      [
        0,
        0,
        0,
        0,
        1,
        1
      ],
      [
        0,
        0,
        0,
        0,
        1,
        1
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "Grade 1 terminator",
    "family": "indicators",
    "braille": [
      [
        0,
        0,
        0,
        0,
        1,
        1
      ],
      [
        0,
        0,
        1,
        0,
        0,
        0
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "italic symbol",
    "family": "indicators",
    "braille": [
      [
        0,
        0,
        0,
        1,
        0,
        1
      ],
      [
        0,
        1,
        1,
        0,
        0,
        0
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "italic word",
    "family": "indicators",
    "braille": [
      [
        0,
        0,
        0,
        1,
        0,
        1
      ],
      [
        0,
        1,
        0,
        0,
        0,
        0
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "italic passage",
    "family": "indicators",
    "braille": [
      [
        0,
        0,
        0,
        1,
        0,
        1
      ],
      [
        0,
        1,
        1,
        0,
        1,
        1
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "italic terminator",
    "family": "indicators",
    "braille": [
      [
        0,
        0,
        0,
        1,
        0,
        1
      ],
      [
        0,
        0,
        1,
        0,
        0,
        0
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "bold symbol",
    "family": "indicators",
    "braille": [
      [
        0,
        0,
        0,
        1,
        1,
        0
      ],
      [
        0,
        1,
        1,
        0,
        0,
        0
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "bold word",
    "family": "indicators",
    "braille": [
      [
        0,
        0,
        0,
        1,
        1,
        0
      ],
      [
        0,
        1,
        0,
        0,
        0,
        0
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "bold passage",
    "family": "indicators",
    "braille": [
      [
        0,
        0,
        0,
        1,
        1,
        0
      ],
      [
        0,
        1,
        1,
        0,
        1,
        1
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "bold terminator",
    "family": "indicators",
    "braille": [
      [
        0,
        0,
        0,
        1,
        1,
        0
      ],
      [
        0,
        0,
        1,
        0,
        0,
        0
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "underline symbol",
    "family": "indicators",
    "braille": [
      [
        0,
        0,
        0,
        1,
        1,
        1
      ],
      [
        0,
        1,
        1,
        0,
        0,
        0
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "underline word",
    "family": "indicators",
    "braille": [
      [
        0,
        0,
        0,
        1,
        1,
        1
      ],
      [
        0,
        1,
        0,
        0,
        0,
        0
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "underline passage",
    "family": "indicators",
    "braille": [
      [
        0,
        0,
        0,
        1,
        1,
        1
      ],
      [
        0,
        1,
        1,
        0,
        1,
        1
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "underline terminator",
    "family": "indicators",
    "braille": [
      [
        0,
        0,
        0,
        1,
        1,
        1
      ],
      [
        0,
        0,
        1,
        0,
        0,
        0
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "script symbol",
    "family": "indicators",
    "braille": [
      [
        0,
        0,
        0,
        1,
        0,
        0
      ],
      [
        0,
        1,
        1,
        0,
        0,
        0
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "script word",
    "family": "indicators",
    "braille": [
      [
        0,
        0,
        0,
        1,
        0,
        0
      ],
      [
        0,
        1,
        0,
        0,
        0,
        0
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "script passage",
    "family": "indicators",
    "braille": [
      [
        0,
        0,
        0,
        1,
        0,
        0
      ],
      [
        0,
        1,
        1,
        0,
        1,
        1
      ],
      [
        0,
        0,
        0,
        0,
        0,
        0
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "script terminator",
    "family": "indicators",
    "braille": [
      [
        0,
        0,
        0,
        1,
        0,
        0
      ],
      [
        0,
        0,
        1,
        0,
        0,
        0
      ]
    ]
  },
  {
    "character": ",",
    "description": "comma",
    "family": "punctuation",
    "braille": [
      [
        0,
        1,
        0,
        0,
        0,
        0
      ]
    ]
  },
  {
    "character": ".",
    "description": "period",
    "family": "punctuation",
    "braille": [
      [
        0,
        1,
        0,
        0,
        1,
        1
      ]
    ]
  },
  {
    "character": "‘",
    "description": "apostrophe",
    "family": "punctuation",
    "braille": [
      [
        0,
        0,
        1,
        0,
        0,
        0
      ]
    ]
  },
  {
    "character": ":",
    "description": "colon",
    "family": "punctuation",
    "braille": [
      [
        0,
        1,
        0,
        1,
        0,
        0
      ]
    ]
  },
  {
    "character": "-",
    "description": "dash",
    "family": "punctuation",
    "braille": [
      [
        0,
        0,
        0,
        0,
        0,
        1
      ],
      [
        0,
        0,
        1,
        0,
        0,
        1
      ]
    ]
  },
  {
    "character": "--",
    "description": "long dash",
    "family": "punctuation",
    "braille": [
      [
        0,
        0,
        0,
        0,
        1,
        0
      ],
      [
        0,
        0,
        0,
        0,
        0,
        1
      ],
      [
        0,
        0,
        1,
        0,
        0,
        1
      ]
    ]
  },
  {
    "character": "!",
    "description": "exclamation mark",
    "family": "punctuation",
    "braille": [
      [
        0,
        1,
        1,
        0,
        1,
        0
      ]
    ]
  },
  {
    "character": "-",
    "description": "hyphen",
    "family": "punctuation",
    "braille": [
      [
        0,
        0,
        1,
        0,
        0,
        1
      ]
    ]
  },
  {
    "character": "?",
    "description": "question mark",
    "family": "punctuation",
    "braille": [
      [
        0,
        1,
        1,
        0,
        0,
        1
      ]
    ]
  },
  {
    "character": ";",
    "description": "semicolon",
    "family": "punctuation",
    "braille": [
      [
        0,
        1,
        1,
        0,
        0,
        0
      ]
    ]
  },
  {
    "character": "...",
    "description": "ellipsis",
    "family": "punctuation",
    "braille": [
      [
        0,
        1,
        0,
        0,
        1,
        1
      ],
      [
        0,
        1,
        0,
        0,
        1,
        1
      ],
      [
        0,
        1,
        0,
        0,
        1,
        1
      ]
    ]
  },
  {
    "character": "/",
    "description": "forward slash",
    "family": "punctuation",
    "braille": [
      [
        0,
        0,
        0,
        1,
        1,
        1
      ],
      [
        0,
        0,
        1,
        1,
        0,
        0
      ]
    ]
  },
  {
    "character": "\\",
    "description": "backward slash",
    "family": "punctuation",
    "braille": [
      [
        0,
        0,
        0,
        1,
        1,
        1
      ],
      [
        1,
        0,
        0,
        0,
        0,
        1
      ]
    ]
  },
  {
    "character": "“",
    "description": "opening outer quotation mark",
    "family": "punctuation",
    "braille": [
      [
        0,
        1,
        1,
        0,
        0,
        1
      ]
    ]
  },
  {
    "character": "”",
    "description": "closing outer quotation mark",
    "family": "punctuation",
    "braille": [
      [
        0,
        0,
        1,
        0,
        1,
        1
      ]
    ]
  },
  {
    "character": "‘",
    "description": "opening inner quotation mark ",
    "family": "punctuation",
    "braille": [
      [
        0,
        0,
        0,
        0,
        0,
        1
      ],
      [
        0,
        1,
        1,
        0,
        0,
        1
      ]
    ]
  },
  {
    "character": "’",
    "description": "closing inner quotation mark",
    "family": "punctuation",
    "braille": [
      [
        0,
        0,
        0,
        0,
        0,
        1
      ],
      [
        0,
        0,
        1,
        0,
        1,
        1
      ]
    ]
  },
  {
    "character": "(",
    "description": "opening round parenthesis",
    "family": "Grouping Punctuation",
    "braille": [
      [
        0,
        0,
        0,
        0,
        1,
        0
      ],
      [
        1,
        1,
        0,
        0,
        0,
        1
      ]
    ]
  },
  {
    "character": ")",
    "description": "closing round parenthesis",
    "family": "Grouping Punctuation",
    "braille": [
      [
        0,
        0,
        0,
        0,
        1,
        0
      ],
      [
        0,
        0,
        1,
        1,
        1,
        0
      ]
    ]
  },
  {
    "character": "[",
    "description": "opening square bracket",
    "family": "Grouping Punctuation",
    "braille": [
      [
        0,
        0,
        0,
        1,
        0,
        1
      ],
      [
        1,
        1,
        0,
        0,
        0,
        1
      ]
    ]
  },
  {
    "character": "]",
    "description": "closing square bracket",
    "family": "Grouping Punctuation",
    "braille": [
      [
        0,
        0,
        0,
        1,
        0,
        1
      ],
      [
        0,
        0,
        1,
        1,
        1,
        0
      ]
    ]
  },
  {
    "character": "{",
    "description": "opening curly bracket",
    "family": "Grouping Punctuation",
    "braille": [
      [
        0,
        0,
        0,
        1,
        1,
        1
      ],
      [
        1,
        1,
        0,
        0,
        0,
        1
      ]
    ]
  },
  {
    "character": "}",
    "description": "closing curly bracket",
    "family": "Grouping Punctuation",
    "braille": [
      [
        0,
        0,
        0,
        1,
        1,
        1
      ],
      [
        0,
        0,
        1,
        1,
        1,
        0
      ]
    ]
  },
  {
    "character": "<",
    "description": "opening angle bracket",
    "family": "Grouping Punctuation",
    "braille": [
      [
        0,
        0,
        0,
        1,
        0,
        0
      ],
      [
        1,
        1,
        0,
        0,
        0,
        1
      ]
    ]
  },
  {
    "character": ">",
    "description": "closing angle bracket",
    "family": "Grouping Punctuation",
    "braille": [
      [
        0,
        0,
        0,
        1,
        0,
        0
      ],
      [
        0,
        0,
        1,
        1,
        1,
        0
      ]
    ]
  },
  {
    "character": "+",
    "description": "plus",
    "family": "Signs Of Operation And Comparison",
    "braille": [
      [
        0,
        0,
        0,
        0,
        1,
        0
      ],
      [
        0,
        1,
        1,
        0,
        1,
        0
      ]
    ]
  },
  {
    "character": "-",
    "description": "minus",
    "family": "Signs Of Operation And Comparison",
    "braille": [
      [
        0,
        0,
        0,
        0,
        1,
        0
      ],
      [
        0,
        0,
        0,
        0,
        1,
        1
      ]
    ]
  },
  {
    "character": "X",
    "description": "multiplication",
    "family": "Signs Of Operation And Comparison",
    "braille": [
      [
        0,
        0,
        0,
        0,
        1,
        0
      ],
      [
        0,
        1,
        1,
        0,
        0,
        1
      ]
    ]
  },
  {
    "character": "·",
    "description": "multiplication dot",
    "family": "Signs Of Operation And Comparison",
    "braille": [
      [
        0,
        0,
        0,
        0,
        1,
        0
      ],
      [
        0,
        1,
        0,
        0,
        1,
        1
      ]
    ]
  },
  {
    "character": "÷",
    "description": "division",
    "family": "Signs Of Operation And Comparison",
    "braille": [
      [
        0,
        0,
        0,
        0,
        1,
        0
      ],
      [
        0,
        0,
        1,
        1,
        0,
        0
      ]
    ]
  },
  {
    "character": ">",
    "description": "greater than",
    "family": "Signs Of Operation And Comparison",
    "braille": [
      [
        0,
        0,
        0,
        1,
        0,
        0
      ],
      [
        0,
        0,
        1,
        1,
        1,
        0
      ]
    ]
  },
  {
    "character": "<",
    "description": "less than",
    "family": "Signs Of Operation And Comparison",
    "braille": [
      [
        0,
        0,
        0,
        1,
        0,
        0
      ],
      [
        1,
        1,
        0,
        0,
        0,
        1
      ]
    ]
  },
  {
    "character": "=",
    "description": "equals",
    "family": "Signs Of Operation And Comparison",
    "braille": [
      [
        0,
        0,
        0,
        1,
        0,
        0
      ],
      [
        0,
        1,
        1,
        0,
        1,
        1
      ]
    ]
  },
  {
    "character": "¢",
    "description": "cent",
    "family": "Currency And Measurement",
    "braille": [
      [
        0,
        0,
        0,
        1,
        0,
        0
      ],
      [
        1,
        0,
        0,
        1,
        0,
        0
      ]
    ]
  },
  {
    "character": "$",
    "description": "dollar",
    "family": "Currency And Measurement",
    "braille": [
      [
        0,
        0,
        0,
        1,
        0,
        0
      ],
      [
        0,
        1,
        1,
        1,
        0,
        0
      ]
    ]
  },
  {
    "character": "€",
    "description": "euro",
    "family": "Currency And Measurement",
    "braille": [
      [
        0,
        0,
        0,
        1,
        0,
        0
      ],
      [
        1,
        0,
        0,
        0,
        1,
        0
      ]
    ]
  },
  {
    "character": "£",
    "description": "British Pound",
    "family": "Currency And Measurement",
    "braille": [
      [
        0,
        0,
        0,
        1,
        0,
        0
      ],
      [
        1,
        1,
        1,
        0,
        0,
        0
      ]
    ]
  },
  {
    "character": "‘",
    "description": "feet",
    "family": "Currency And Measurement",
    "braille": [
      [
        0,
        1,
        1,
        0,
        1,
        1
      ]
    ]
  },
  {
    "character": "“",
    "description": "inches",
    "family": "Currency And Measurement",
    "braille": [
      [
        0,
        1,
        1,
        0,
        1,
        1
      ],
      [
        0,
        1,
        1,
        0,
        1,
        1
      ]
    ]
  },
  {
    "character": "%",
    "description": "percent",
    "family": "Special Symbols",
    "braille": [
      [
        0,
        0,
        0,
        1,
        0,
        1
      ],
      [
        0,
        0,
        1,
        0,
        1,
        1
      ]
    ]
  },
  {
    "character": "°",
    "description": "degree",
    "family": "Special Symbols",
    "braille": [
      [
        0,
        0,
        0,
        1,
        1,
        0
      ],
      [
        0,
        1,
        0,
        1,
        1,
        0
      ]
    ]
  },
  {
    "character": "⦣",
    "description": "angle",
    "family": "Special Symbols",
    "braille": [
      [
        0,
        0,
        0,
        1,
        1,
        1
      ],
      [
        0,
        1,
        0,
        1,
        0,
        1
      ]
    ]
  },
  {
    "character": "#",
    "description": "hashtag",
    "family": "Special Symbols",
    "braille": [
      [
        0,
        0,
        0,
        1,
        1,
        1
      ],
      [
        1,
        0,
        0,
        1,
        1,
        1
      ]
    ]
  },
  {
    "character": "&",
    "description": "ampersand",
    "family": "Special Symbols",
    "braille": [
      [
        0,
        0,
        0,
        1,
        0,
        0
      ],
      [
        1,
        1,
        1,
        1,
        0,
        1
      ]
    ]
  },
  {
    "character": "©",
    "description": "copyright",
    "family": "Special Symbols",
    "braille": [
      [
        0,
        0,
        0,
        1,
        1,
        0
      ],
      [
        1,
        0,
        0,
        1,
        0,
        0
      ]
    ]
  },
  {
    "character": "™",
    "description": "trademark",
    "family": "Special Symbols",
    "braille": [
      [
        0,
        0,
        0,
        1,
        1,
        0
      ],
      [
        0,
        1,
        1,
        1,
        1,
        0
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "superscript indicator",
    "family": "Special Symbols",
    "braille": [
      [
        0,
        0,
        1,
        0,
        1,
        0
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "subscript indicator",
    "family": "Special Symbols",
    "braille": [
      [
        0,
        1,
        0,
        0,
        0,
        1
      ]
    ]
  },
  {
    "character": "·",
    "description": "bullet",
    "family": "Special Symbols",
    "braille": [
      [
        0,
        0,
        0,
        1,
        1,
        1
      ],
      [
        0,
        1,
        0,
        0,
        1,
        1
      ]
    ]
  },
  {
    "character": "@",
    "description": "at sign ",
    "family": "Special Symbols",
    "braille": [
      [
        0,
        0,
        0,
        1,
        0,
        0
      ],
      [
        1,
        0,
        0,
        0,
        0,
        0
      ]
    ]
  },
  {
    "character": "*",
    "description": "asterisk",
    "family": "Special Symbols",
    "braille": [
      [
        0,
        0,
        0,
        0,
        1,
        0
      ],
      [
        0,
        0,
        1,
        0,
        1,
        0
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "dot locator for mention",
    "family": "Special Symbols",
    "braille": [
      [
        0,
        0,
        0,
        1,
        0,
        1
      ],
      [
        1,
        1,
        1,
        1,
        1,
        1
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "ch",
    "family": "Strong Groupsigns",
    "braille": [
      [
        1,
        0,
        0,
        0,
        0,
        1
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "sh",
    "family": "Strong Groupsigns",
    "braille": [
      [
        1,
        0,
        0,
        1,
        0,
        1
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "th",
    "family": "Strong Groupsigns",
    "braille": [
      [
        1,
        0,
        0,
        1,
        1,
        1
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "wh",
    "family": "Strong Groupsigns",
    "braille": [
      [
        1,
        0,
        0,
        0,
        1,
        1
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "ou",
    "family": "Strong Groupsigns",
    "braille": [
      [
        1,
        1,
        0,
        0,
        1,
        1
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "st",
    "family": "Strong Groupsigns",
    "braille": [
      [
        0,
        0,
        1,
        1,
        0,
        0
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "gh",
    "family": "Strong Groupsigns",
    "braille": [
      [
        1,
        1,
        0,
        0,
        0,
        1
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "ed",
    "family": "Strong Groupsigns",
    "braille": [
      [
        1,
        1,
        0,
        1,
        0,
        1
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "er",
    "family": "Strong Groupsigns",
    "braille": [
      [
        1,
        1,
        0,
        1,
        1,
        1
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "ow",
    "family": "Strong Groupsigns",
    "braille": [
      [
        0,
        1,
        0,
        1,
        0,
        1
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "ar",
    "family": "Strong Groupsigns",
    "braille": [
      [
        0,
        0,
        1,
        1,
        1,
        0
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "ing",
    "family": "Strong Groupsigns",
    "braille": [
      [
        0,
        0,
        1,
        1,
        0,
        1
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "ea",
    "family": "Lower Groupsigns",
    "braille": [
      [
        0,
        1,
        0,
        0,
        0,
        0
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "bb",
    "family": "Lower Groupsigns",
    "braille": [
      [
        0,
        1,
        1,
        0,
        0,
        0
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "cc",
    "family": "Lower Groupsigns",
    "braille": [
      [
        0,
        1,
        0,
        0,
        1,
        0
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "ff",
    "family": "Lower Groupsigns",
    "braille": [
      [
        0,
        1,
        1,
        0,
        1,
        0
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "gg",
    "family": "Lower Groupsigns",
    "braille": [
      [
        0,
        1,
        1,
        0,
        1,
        1
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "be",
    "family": "Strong Contractions (Part and Whole Word)",
    "braille": [
      [
        0,
        1,
        1,
        0,
        0,
        0
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "con",
    "family": "Strong Contractions (Part and Whole Word)",
    "braille": [
      [
        0,
        1,
        0,
        1,
        0,
        0
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "dis",
    "family": "Strong Contractions (Part and Whole Word)",
    "braille": [
      [
        0,
        1,
        0,
        0,
        1,
        1
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "en",
    "family": "Strong Contractions (Part and Whole Word)",
    "braille": [
      [
        0,
        1,
        0,
        0,
        0,
        1
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "in",
    "family": "Strong Contractions (Part and Whole Word)",
    "braille": [
      [
        0,
        0,
        1,
        0,
        1,
        0
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "be",
    "family": "Lower Wordsigns",
    "braille": [
      [
        0,
        1,
        1,
        0,
        0,
        0
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "enough",
    "family": "Lower Wordsigns",
    "braille": [
      [
        0,
        1,
        0,
        0,
        0,
        1
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "were",
    "family": "Lower Wordsigns",
    "braille": [
      [
        0,
        1,
        1,
        0,
        1,
        1
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "his",
    "family": "Lower Wordsigns",
    "braille": [
      [
        0,
        1,
        1,
        0,
        0,
        1
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "in",
    "family": "Lower Wordsigns",
    "braille": [
      [
        0,
        0,
        1,
        0,
        1,
        0
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "was",
    "family": "Lower Wordsigns",
    "braille": [
      [
        0,
        0,
        1,
        0,
        1,
        1
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "child",
    "family": "Strong Wordsigns",
    "braille": [
      [
        1,
        0,
        0,
        0,
        0,
        1
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "shall",
    "family": "Strong Wordsigns",
    "braille": [
      [
        1,
        0,
        0,
        1,
        0,
        1
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "this",
    "family": "Strong Wordsigns",
    "braille": [
      [
        1,
        0,
        0,
        1,
        1,
        1
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "which",
    "family": "Strong Wordsigns",
    "braille": [
      [
        1,
        0,
        0,
        0,
        1,
        1
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "out",
    "family": "Strong Wordsigns",
    "braille": [
      [
        1,
        1,
        0,
        0,
        1,
        1
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "still",
    "family": "Strong Wordsigns",
    "braille": [
      [
        0,
        0,
        1,
        1,
        0,
        0
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "and",
    "family": "Strong Contractions (Part and Whole Word)",
    "braille": [
      [
        1,
        1,
        1,
        1,
        0,
        1
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "for",
    "family": "Strong Contractions (Part and Whole Word)",
    "braille": [
      [
        1,
        1,
        1,
        1,
        1,
        1
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "of",
    "family": "Strong Contractions (Part and Whole Word)",
    "braille": [
      [
        1,
        1,
        1,
        0,
        1,
        1
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "the",
    "family": "Strong Contractions (Part and Whole Word)",
    "braille": [
      [
        0,
        1,
        1,
        1,
        0,
        1
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "with",
    "family": "Strong Contractions (Part and Whole Word)",
    "braille": [
      [
        0,
        1,
        1,
        1,
        1,
        1
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "day",
    "family": "Initial Letter Contractions",
    "braille": [
      [
        0,
        0,
        0,
        0,
        1,
        0
      ],
      [
        1,
        0,
        0,
        1,
        1,
        0
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "ever",
    "family": "Initial Letter Contractions",
    "braille": [
      [
        0,
        0,
        0,
        0,
        1,
        0
      ],
      [
        1,
        0,
        0,
        0,
        1,
        0
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "father",
    "family": "Initial Letter Contractions",
    "braille": [
      [
        0,
        0,
        0,
        0,
        1,
        0
      ],
      [
        1,
        1,
        0,
        1,
        0,
        0
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "here",
    "family": "Initial Letter Contractions",
    "braille": [
      [
        0,
        0,
        0,
        0,
        1,
        0
      ],
      [
        1,
        1,
        0,
        0,
        1,
        0
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "know",
    "family": "Initial Letter Contractions",
    "braille": [
      [
        0,
        0,
        0,
        0,
        1,
        0
      ],
      [
        1,
        0,
        1,
        0,
        0,
        0
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "lord",
    "family": "Initial Letter Contractions",
    "braille": [
      [
        0,
        0,
        0,
        0,
        1,
        0
      ],
      [
        1,
        1,
        1,
        0,
        0,
        0
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "mother",
    "family": "Initial Letter Contractions",
    "braille": [
      [
        0,
        0,
        0,
        0,
        1,
        0
      ],
      [
        1,
        0,
        1,
        1,
        0,
        0
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "name",
    "family": "Initial Letter Contractions",
    "braille": [
      [
        0,
        0,
        0,
        0,
        1,
        0
      ],
      [
        1,
        0,
        1,
        1,
        0,
        0
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "one",
    "family": "Initial Letter Contractions",
    "braille": [
      [
        0,
        0,
        0,
        0,
        1,
        0
      ],
      [
        1,
        0,
        1,
        0,
        1,
        0
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "part",
    "family": "Initial Letter Contractions",
    "braille": [
      [
        0,
        0,
        0,
        0,
        1,
        0
      ],
      [
        1,
        1,
        1,
        0,
        1,
        0
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "question",
    "family": "Initial Letter Contractions",
    "braille": [
      [
        0,
        0,
        0,
        0,
        1,
        0
      ],
      [
        1,
        1,
        1,
        1,
        1,
        0
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "right",
    "family": "Initial Letter Contractions",
    "braille": [
      [
        0,
        0,
        0,
        0,
        1,
        0
      ],
      [
        1,
        1,
        1,
        0,
        1,
        0
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "some",
    "family": "Initial Letter Contractions",
    "braille": [
      [
        0,
        0,
        0,
        0,
        1,
        0
      ],
      [
        0,
        1,
        1,
        1,
        0,
        0
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "time",
    "family": "Initial Letter Contractions",
    "braille": [
      [
        0,
        0,
        0,
        0,
        1,
        0
      ],
      [
        0,
        1,
        1,
        1,
        1,
        0
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "under",
    "family": "Initial Letter Contractions",
    "braille": [
      [
        0,
        0,
        0,
        0,
        1,
        0
      ],
      [
        1,
        0,
        1,
        0,
        0,
        1
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "work",
    "family": "Initial Letter Contractions",
    "braille": [
      [
        0,
        0,
        0,
        0,
        1,
        0
      ],
      [
        0,
        1,
        0,
        1,
        1,
        1
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "young",
    "family": "Initial Letter Contractions",
    "braille": [
      [
        0,
        0,
        0,
        0,
        1,
        0
      ],
      [
        1,
        0,
        1,
        1,
        1,
        1
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "there",
    "family": "Initial Letter Contractions",
    "braille": [
      [
        0,
        0,
        0,
        0,
        1,
        0
      ],
      [
        0,
        1,
        1,
        1,
        0,
        1
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "character",
    "family": "Initial Letter Contractions",
    "braille": [
      [
        0,
        0,
        0,
        0,
        1,
        0
      ],
      [
        1,
        0,
        0,
        0,
        0,
        1
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "through",
    "family": "Initial Letter Contractions",
    "braille": [
      [
        0,
        0,
        0,
        0,
        1,
        0
      ],
      [
        1,
        0,
        0,
        1,
        1,
        1
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "where",
    "family": "Initial Letter Contractions",
    "braille": [
      [
        0,
        0,
        0,
        0,
        1,
        0
      ],
      [
        1,
        0,
        0,
        0,
        1,
        1
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "ought",
    "family": "Initial Letter Contractions",
    "braille": [
      [
        0,
        0,
        0,
        0,
        1,
        0
      ],
      [
        1,
        1,
        0,
        0,
        1,
        1
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "upon",
    "family": "Initial Letter Contractions",
    "braille": [
      [
        0,
        0,
        0,
        1,
        1,
        0
      ],
      [
        1,
        0,
        1,
        0,
        0,
        1
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "word",
    "family": "Initial Letter Contractions",
    "braille": [
      [
        0,
        0,
        0,
        1,
        1,
        0
      ],
      [
        0,
        1,
        0,
        1,
        1,
        1
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "these",
    "family": "Initial Letter Contractions",
    "braille": [
      [
        0,
        0,
        0,
        1,
        1,
        0
      ],
      [
        0,
        1,
        1,
        1,
        0,
        1
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "those",
    "family": "Initial Letter Contractions",
    "braille": [
      [
        0,
        0,
        0,
        1,
        1,
        0
      ],
      [
        1,
        0,
        0,
        1,
        1,
        1
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "whose",
    "family": "Initial Letter Contractions",
    "braille": [
      [
        0,
        0,
        0,
        1,
        1,
        0
      ],
      [
        1,
        0,
        0,
        0,
        1,
        1
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "cannot",
    "family": "Initial Letter Contractions",
    "braille": [
      [
        0,
        0,
        0,
        1,
        1,
        1
      ],
      [
        1,
        0,
        0,
        1,
        0,
        0
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "had",
    "family": "Initial Letter Contractions",
    "braille": [
      [
        0,
        0,
        0,
        1,
        1,
        1
      ],
      [
        1,
        1,
        0,
        1,
        0,
        0
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "many",
    "family": "Initial Letter Contractions",
    "braille": [
      [
        0,
        0,
        0,
        1,
        1,
        1
      ],
      [
        1,
        0,
        1,
        1,
        0,
        0
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "spirit",
    "family": "Initial Letter Contractions",
    "braille": [
      [
        1,
        1,
        1,
        0,
        0,
        0
      ],
      [
        0,
        1,
        1,
        1,
        0,
        0
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "world",
    "family": "Initial Letter Contractions",
    "braille": [
      [
        0,
        0,
        0,
        1,
        1,
        1
      ],
      [
        0,
        1,
        0,
        1,
        1,
        1
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "their",
    "family": "Initial Letter Contractions",
    "braille": [
      [
        0,
        0,
        0,
        1,
        1,
        1
      ],
      [
        0,
        1,
        1,
        1,
        0,
        1
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "ound",
    "family": "Final Letter Group Signs",
    "braille": [
      [
        0,
        0,
        0,
        1,
        0,
        1
      ],
      [
        1,
        0,
        0,
        1,
        1,
        0
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "ance",
    "family": "Final Letter Group Signs",
    "braille": [
      [
        0,
        0,
        0,
        1,
        0,
        1
      ],
      [
        1,
        0,
        0,
        1,
        1,
        0
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "sion",
    "family": "Final Letter Group Signs",
    "braille": [
      [
        0,
        0,
        0,
        1,
        0,
        1
      ],
      [
        1,
        0,
        1,
        1,
        1,
        0
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "less",
    "family": "Final Letter Group Signs",
    "braille": [
      [
        0,
        0,
        0,
        1,
        0,
        1
      ],
      [
        0,
        1,
        1,
        1,
        0,
        0
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "ount",
    "family": "Final Letter Group Signs",
    "braille": [
      [
        0,
        0,
        0,
        1,
        0,
        1
      ],
      [
        0,
        1,
        1,
        1,
        1,
        0
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "ence",
    "family": "Final Letter Group Signs",
    "braille": [
      [
        0,
        0,
        0,
        0,
        1,
        1
      ],
      [
        1,
        0,
        0,
        0,
        1,
        0
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "ong",
    "family": "Final Letter Group Signs",
    "braille": [
      [
        0,
        0,
        0,
        0,
        1,
        1
      ],
      [
        1,
        1,
        0,
        1,
        1,
        0
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "ful",
    "family": "Final Letter Group Signs",
    "braille": [
      [
        0,
        0,
        0,
        0,
        1,
        1
      ],
      [
        1,
        1,
        1,
        0,
        0,
        0
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "tion",
    "family": "Final Letter Group Signs",
    "braille": [
      [
        0,
        0,
        0,
        0,
        1,
        1
      ],
      [
        1,
        0,
        1,
        1,
        1,
        0
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "ness",
    "family": "Final Letter Group Signs",
    "braille": [
      [
        0,
        0,
        0,
        0,
        1,
        1
      ],
      [
        0,
        1,
        1,
        1,
        0,
        0
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "ment",
    "family": "Final Letter Group Signs",
    "braille": [
      [
        0,
        0,
        0,
        0,
        1,
        1
      ],
      [
        0,
        1,
        1,
        1,
        1,
        0
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "ity",
    "family": "Final Letter Group Signs",
    "braille": [
      [
        0,
        0,
        0,
        0,
        1,
        1
      ],
      [
        1,
        0,
        1,
        1,
        1,
        1
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "ble",
    "family": "Retired Contractions",
    "braille": [
      [
        0,
        0,
        1,
        1,
        1,
        1
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "dd",
    "family": "Retired Contractions",
    "braille": [
      [
        0,
        1,
        0,
        0,
        1,
        1
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "into",
    "family": "Retired Contractions",
    "braille": [
      [
        0,
        0,
        1,
        0,
        1,
        0
      ],
      [
        0,
        1,
        1,
        0,
        1,
        0
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "ation",
    "family": "Retired Contractions",
    "braille": [
      [
        0,
        0,
        0,
        0,
        0,
        1
      ],
      [
        1,
        0,
        1,
        1,
        1,
        0
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "com",
    "family": "Retired Contractions",
    "braille": [
      [
        0,
        0,
        0,
        1,
        0,
        1
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "by",
    "family": "Retired Contractions",
    "braille": [
      [
        0,
        0,
        1,
        1,
        1,
        0
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "ally",
    "family": "Retired Contractions",
    "braille": [
      [
        0,
        0,
        0,
        0,
        0,
        1
      ],
      [
        1,
        0,
        1,
        1,
        1,
        1
      ]
    ]
  },
  {
    "character": "not applicable",
    "description": "to",
    "family": "Retired Contractions",
    "braille": [
      [
        0,
        1,
        1,
        0,
        1,
        0
      ]
    ]
  }
]

    human_readable = convert(data)

    with open("output.csv", 'w') as f:
        headers = ["Family","Description","Character","cell 1","cell 2","cell 3","Readable Braille"]
        csv_data = [headers]

        for d in human_readable:
            csv_data.append([d[h] for h in headers])

        writer = csv.writer(f)
        writer.writerows(csv_data)


if __name__ == '__main__':
    main()