test = {
  'name': 'Problem 5',
  'points': 150,
  'suites': [
    {
      'cases': [
        {
          'answer': 'Pair(A, nil), where: A is the quoted expression',
          'choices': [
            r"""
            Pair('quote', Pair(A, nil)), where:
                A is the quoted expression
            """,
            r"""
            [A], where:
                A is the quoted expression
            """,
            r"""
            Pair(A, nil), where:
                A is the quoted expression
            """,
            r"""
            A, where:
                A is the quoted expression
            """
          ],
          'hidden': False,
          'locked': False,
          'multiline': False,
          'question': 'What is the structure of the expressions argument to do_quote_form?'
        }
      ],
      'scored': False,
      'type': 'concept'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> do_quote_form(Pair(3, nil), global_frame)
          3
          >>> do_quote_form(Pair('hi', nil), global_frame)
          'hi'
          >>> expr = Pair(Pair('+', Pair('x', Pair(2, nil))), nil)
          >>> do_quote_form(expr, global_frame) # Make sure to use Pair notation
          Pair('+', Pair('x', Pair(2, nil)))
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from scheme import *
      >>> global_frame = create_global_frame()
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          scm> ''hello
          (quote hello)
          scm> (quote (1 2))
          (1 2)
          scm> (car '(1 2 3))
          1
          scm> (cdr '(1 2))
          (2)
          scm> (cons 'car '('(4 2)))
          2234c2efce8aa029eaab9df8f6431f75
          # locked
          scm> (eval (cons 'car '('(4 2))))
          46beb7deeeb5e9af1c8d785b12558317
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'scheme'
    },
    {
      'cases': [
        {
          'code': r"""
          scm> (quote hello)
          hello
          scm> 'hello
          hello
          scm> ''hello
          (quote hello)
          scm> (quote (1 2))
          (1 2)
          scm> '(1 2)
          (1 2)
          scm> (car (car '((1))))
          1
          scm> (quote 3)
          3
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
