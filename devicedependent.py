
models = [
  'QL-500',
  'QL-550',
  'QL-560',
  'QL-570',
  'QL-580N',
  'QL-650TD'
  'QL-700',
  'QL-710W',
  'QL-720NW',
  'QL-1050',
  'QL-1060N',
]

min_max_length_dots = {
  'default':  (295, 11811),

  # 'QL-500', 'QL-550', 'QL-560', and 'QL-650TD'
  # they all use the default.

  'QL-1050':  (295, 35433),
  'QL-1060N': (295, 35433),

  'QL-570':   (150, 11811),
  'QL-580N':  (150, 11811),
  'QL-700':   (150, 11811),
  'QL-710W':  (150, 11811),
  'QL-720NW': (150, 11811),
}

min_max_feed = {
  'default':  (35, 1500),
}

paper_dimensions = {
  # the dimensions are given as (width, length)
  # tape with length  >  0: rectangular die-cut labels
  # tape with length ==  0: continuous length tape
  # tape with length == -1: round die-cut labels
  #ID: ( tape_size_mm,  size_dots,    printable size dots, right_margin_dots, restrict_printers)
  257:     ((12,   0),  (142,    0),  (106,   0),  29, []),
  258:     ((29,   0),  (342,    0),  (306,   0),   6, []),
  264:     ((38,   0),  (449,    0),  (413,   0),  12, []),
  262:     ((50,   0),  (590,    0),  (554,   0),  12, []),
  261:     ((54,   0),  (636,    0),  (590,   0),   0, []),
  259:     ((62,   0),  (732,    0),  (696,   0),  12, []),
  260:    ((102,   0), (1200,    0), (1164,   0),  12, ['QL-1060N', 'QL-1050']),
  
  269:     ((17,  54),  (201,  636),  (165,  566),   0, []),
  270:     ((17,  87),  (201, 1026),  (165,  956),   0, []),
  370:     ((23,  23),  (272,  272),  (202,  202),  42, []),
  358:     ((29,  42),  (342,  495),  (306,  425),   6, []),
  271:     ((29,  90),  (342, 1061),  (306,  991),   6, []),
  272:     ((38,  90),  (449, 1061),  (413,  991),  12, []),
  367:     ((39,  48),  (461,  565),  (425,  495),   6, []),
  374:     ((52,  29),  (614,  341),  (578,  271),   0, []),
  274:     ((62,  29),  (732,  341),  (696,  271),  12, []),
  275:     ((62, 100),  (732, 1179),  (696, 1109),  12, []),
  365:    ((102,  51), (1200,  596), (1164,  526),  12, ['QL-1060N', 'QL-1050']),
  366:    ((102, 152), (1200, 1804), (1164, 1660),  12, ['QL-1060N', 'QL-1050']),
  362:     ((12,  -1),  (142,  142),  ( 94,   94), 113, []),
  363:     ((24,  -1),  (284,  284),  (236,  236),  42, []),
  273:     ((58,  -1),  (688,  688),  (618,  618),  51, []),
}

number_bytes_per_row = {
  'default':   90,
  'QL-1050':  162,
  'QL-1060N': 162,
}

right_margin_addition = {
  'default':   0,
  'QL-1050':  44,
  'QL-1060N': 44,
}
