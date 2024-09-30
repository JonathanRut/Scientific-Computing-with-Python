import copy
import random
# Consider using the modules imported above.

class Hat:

  def __init__(self, **kwargs):
    self.contents = []
    for type, number in kwargs.items():
      for i in range(number):
        self.contents.append(type)

  def draw(self, number):
    if number > len(self.contents):
      return self.contents
    else:
      balls = []
      for i in range(number):
        ball = random.choice(self.contents)
        balls.append(ball)
        self.contents.remove(ball)
      return balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  successes = 0
  for i in range(num_experiments):
    hat_copy = copy.deepcopy(hat)
    balls = hat_copy.draw(num_balls_drawn)
    balls_dict = {}
    for ball in balls:
      balls_dict[ball] = balls_dict.get(ball, 0) + 1
    success = True
    for type, number in expected_balls.items():
      if balls_dict.get(type, 0) < number:
        success = False
        break
    if success:
      successes += 1
  return successes / num_experiments