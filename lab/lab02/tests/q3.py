test = {
  'name': 'Question 3: A, B, and X',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> a = lambda x: x * 2 + 1
          >>> def b(b, x):
          ...     return b(x + a(x))
          >>> x = 3
          >>> b(a, x)
          ec0a028e76255df62e474d61f4ce4c88
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
