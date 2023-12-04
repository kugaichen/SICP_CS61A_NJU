test = {
  'name': 'Question 3: What If?',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> def ab(c, d):
          ...     if c > 5:
          ...         print(c)
          ...     elif c > 7:
          ...         print(d)
          ...     print('foo')
          >>> ab(10, 20)
          2e84fdcfc2629c3d705e5f993880ba93
          cbcbbebf0a6adc63a6dfa2640874f74c
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> def bake(cake, make):
          ...     if cake == 0:
          ...         cake = cake + 1
          ...         print(cake)
          ...     if cake == 1:
          ...         print(make)
          ...     else:
          ...         return cake
          ...     return make
          >>> bake(0, 29)
          a6c04b3abc7fe1ec9a1005943f8d3eb2
          88274383c7f86a17b86d874307d8be4c
          88274383c7f86a17b86d874307d8be4c
          # locked
          >>> bake(1, "mashed potatoes")
          3dfe2a90e7620af5cf5ced4e49ad0933
          61e17c1e3b79311d812c80d9082714f7
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
