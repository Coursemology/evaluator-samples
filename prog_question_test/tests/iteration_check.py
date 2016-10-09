#if iterable it will return True
#else False

def iteration_check(x):
  try: iter(x)
  except TypeError: return False
  else: return True
