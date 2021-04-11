def find_max(input_numbers):
  max = input_numbers[0]
  for number in input_numbers:
    if number > max:
      max = number
  return(max)

