test = {
  'name': 'Question 2: Veritasiness',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> True and 13
          dae13fde9de7642d96519c1e39246ee7
          # locked
          >>> False or 0
          8196893c22d89c9afd3d2108e42da416
          # locked
          >>> not 10
          e8e6987bc93d9346d4867d222cb6acb5
          # locked
          >>> not None
          bdcee028b228d3221c098ab99460c911
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> True and 1 / 0 and False
          cccf412b811f027bfbaaf1f86a916ef4
          # locked
          >>> True or 1 / 0 or False
          bdcee028b228d3221c098ab99460c911
          # locked
          >>> True and 0
          8196893c22d89c9afd3d2108e42da416
          # locked
          >>> False or 1
          a6c04b3abc7fe1ec9a1005943f8d3eb2
          # locked
          >>> 1 and 3 and 6 and 10 and 15
          a55b7ba9ae5f5238dc13d96188584449
          # locked
          >>> 0 or False or 2 or 1 / 0
          006d4591a1bd7a49cba94a3350e16659
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> not 0
          bdcee028b228d3221c098ab99460c911
          # locked
          >>> (1 + 1) and 1
          a6c04b3abc7fe1ec9a1005943f8d3eb2
          # locked
          >>> 1/0 or True
          cccf412b811f027bfbaaf1f86a916ef4
          # locked
          >>> (True or False) and False
          e8e6987bc93d9346d4867d222cb6acb5
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
