def mid(str):
  if len(str) % 2 == 0:
    return ""
  else:
    i = len(str) // 2
    print(str[i])
    return str[i]


mid('Exponential')
