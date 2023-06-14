def read_file(filename=""):
  """
  Reads a text file (UTF8) and prints it to stdout.

  Args:
    filename: The path to the text file.

  Returns:
    None.
  """

  with open(filename, "r", encoding="utf-8") as f:
    for line in f:
      print(line, end="")
