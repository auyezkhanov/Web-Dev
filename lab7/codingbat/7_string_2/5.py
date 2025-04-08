<<<<<<< HEAD

def end_other(a, b):
  if len(a) < len(b):
    return b.lower().endswith(a.lower())
  else:
=======

def end_other(a, b):
  if len(a) < len(b):
    return b.lower().endswith(a.lower())
  else:
>>>>>>> d2f3f40 (commit)
    return a.lower().endswith(b.lower())