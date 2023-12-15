test = {
  'name': 'Question 2: Higher Order Functions',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # If Python displays <function...>, type Function, if it errors type Error, if it displays nothing type Nothing
          >>> def even(f):
          ...     def odd(x):
          ...         if x < 0:
          ...             return f(-x)
          ...         return f(x)
          ...     return odd
          >>> steven = lambda x: x
          >>> stewart = even(steven)
          >>> stewart
          70a755394de50e28a69066f97cacd5d6
          # locked
          >>> stewart(61)
          b925d9ebdbba293bd90b958a207aa5fb
          # locked
          >>> stewart(-4)
          d35d10d14805fc8edf86db641454a218
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> # If Python displays <function...>, type Function, if it errors type Error, if it displays nothing type Nothing
          >>> def cake():
          ...    print('beets')
          ...    def pie():
          ...        print('sweets')
          ...        return 'cake'
          ...    return pie
          >>> chocolate = cake()
          62ecec171ec4fef6328c62541bb20720
          # locked
          >>> chocolate
          70a755394de50e28a69066f97cacd5d6
          # locked
          >>> chocolate()
          3d1ace3a947e26955dd662a65e375de3
          31a2aa055f2ae11504bdf9fdd3424668
          # locked
          >>> more_chocolate, more_cake = chocolate(), cake
          3d1ace3a947e26955dd662a65e375de3
          # locked
          >>> more_chocolate
          31a2aa055f2ae11504bdf9fdd3424668
          # locked
          >>> # Reminder: cake, more_cake, and chocolate were defined/assigned in the code above! 
          >>> # It might be helpful to refer to their definitions on the assignment website so you don't have to scroll as much!
          >>> def snake(x, y):
          ...    if cake == more_cake:
          ...        return chocolate
          ...    else:
          ...        return x + y
          >>> snake(10, 20)
          70a755394de50e28a69066f97cacd5d6
          # locked
          >>> snake(10, 20)()
          3d1ace3a947e26955dd662a65e375de3
          31a2aa055f2ae11504bdf9fdd3424668
          # locked
          >>> cake = 'cake'
          >>> snake(10, 20)
          a9fc36a95eb70f1cdfaa14ffe70d0e9f
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
