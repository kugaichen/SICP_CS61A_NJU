test = {
  'name': 'Question 1: Lambda the Free',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'answer': 'b2cfa01559e8de43f9ad1c088b57ec01',
          'choices': [
            'A lambda expression does not automatically bind the function object that it returns to an intrinsic name.',
            'A lambda expression cannot have more than two parameters.',
            'A lambda expression cannot return another function.',
            'A def statement can only have one line in its body.'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': 'Which of the following statements describes a difference between a def statement and a lambda expression?'
        },
        {
          'answer': '5fbfaaa8a08a232267120f93f3fb47bb',
          'choices': [
            'one',
            'two',
            'three',
            'Not enough information'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': r"""
          How many parameters does the following lambda expression have?
          lambda a, b: c + d
          """
        },
        {
          'answer': 'd646c657e06459b0782595ec498aad13',
          'choices': [
            'When the function returned by the lambda expression is called.',
            'When you assign the lambda expression to a name.',
            'When the lambda expression is evaluated.',
            'When you pass the lambda expression into another function.'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': 'When is the return expression of a lambda expression executed?'
        }
      ],
      'scored': False,
      'type': 'concept'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> # If Python displays <function...>, type Function, if it errors type Error, if it displays nothing type Nothing
          >>> lambda x: x  # A lambda expression with one parameter x
          70a755394de50e28a69066f97cacd5d6
          # locked
          >>> a = lambda x: x  # Assigning a lambda function to the name a
          >>> a(5)
          470cca354530f492f6d6f9b1a2d86c68
          # locked
          >>> (lambda: 3)()  # Using a lambda expression as an operator in a call exp.
          76fda20b7f25aade0e0fb5ea03c991ad
          # locked
          >>> b = lambda x: lambda: x  # Lambdas can return other lambdas!
          >>> c = b(88)
          >>> c
          70a755394de50e28a69066f97cacd5d6
          # locked
          >>> c()
          394543f496c9b615a6d974819af85215
          # locked
          >>> d = lambda f: f(4)  # They can have functions as arguments as well
          >>> def square(x):
          ...     return x * x
          >>> d(square)
          8a0fc1c0a522cdc3ae639dc9c0fc8c83
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> #
          >>> # Pay attention to the scope of variables
          >>> z = 3
          >>> e = lambda x: lambda y: lambda: x + y + z
          >>> e(0)(1)()
          d35d10d14805fc8edf86db641454a218
          # locked
          >>> f = lambda z: x + z
          >>> f(3)
          16eb6121488e6561bc0e0fe641879453
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> x = None # remember to review the rules of WWPD given above!
          >>> x
          97cb946fee9861ac681f2e57a67678e1
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> # Try drawing an environment diagram if you get stuck!
          >>> higher_order_lambda = lambda f: lambda x: f(x)
          >>> g = lambda x: x * x
          >>> higher_order_lambda(2)(g) # Which argument belongs to which function call?
          16eb6121488e6561bc0e0fe641879453
          # locked
          >>> higher_order_lambda(g)(2)
          d35d10d14805fc8edf86db641454a218
          # locked
          >>> call_thrice = lambda f: lambda x: f(f(f(x)))
          >>> call_thrice(lambda y: y + 1)(0)
          76fda20b7f25aade0e0fb5ea03c991ad
          # locked
          >>> print_lambda = lambda z: print(z) # When is the return expression of a lambda expression executed?
          >>> print_lambda
          70a755394de50e28a69066f97cacd5d6
          # locked
          >>> one_thousand = print_lambda(1000)
          4d07f6bd0e1d0e1ec239c2debd0ec859
          # locked
          >>> one_thousand # What did the call to print_lambda return?
          97cb946fee9861ac681f2e57a67678e1
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
