def write(message):
  for char in message:
    sys.stdout.write(char)
    sys.stdout.flush()

    if char != "\n":
      time.sleep(0.06)
    else:
      time.sleep(0.1)
  sys.stdout.write("\n")