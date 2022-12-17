def add_time(start, duration, parameter='x'):

  days = [
    "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday",
    "Sunday"
  ]

  # 11:03 MA => ['11:03','MA'] => ['11','03','MA'] => 11*60 + 30
  aux = start.split()

  l_start = aux[0].split(':')
  start_h = int(l_start[0])
  start_m = int(l_start[1])
  start_AM_PH = aux[1]

  l_duration = duration.split(':')
  duration_h = int(l_duration[0])
  duration_m = int(l_duration[1])

  # verify PM and add 12h
  if start_AM_PH == 'PM':
    start_h = start_h + 12

  # Convert star and duration for minutes and sum
  total = (start_h * 60) + start_m + (duration_h * 60) + duration_m

  #
  cont_days = total // 1440
  rest_days = total % 1440
  new_h = total // 60
  new_m = total % 60

  # Calculate
  if cont_days > 0:
    new_h = rest_days // 60
    new_m = rest_days % 60

  if new_h >= 12 and new_m > 0:
    if new_h > 13:
      new_h = new_h - 12
    new_AM_PM = 'PM'
  else:
    new_AM_PM = 'AM'
    # caso das 00:04 que deve ser 12:04
    if new_h == 0:
      new_h = 12

  # construct new_time
  new_time = str(new_h) + ':' + str(new_m).zfill(2) + ' ' + new_AM_PM
  if parameter != 'x':

    # Calculate the day of the week of the result
    aux_day = cont_days  # days until the result
    aux_index_parameter = days.index(parameter.capitalize())
    if cont_days > 7:
      aux_day = cont_days % 7  # days to result after weekly cycle
    aux_day = aux_day + aux_index_parameter  # result day index
    if aux_day > 6:
      aux_day = aux_day - 7  # result day index
    parameter = days[aux_day]

    new_time = new_time + ', ' + str(parameter)
  if cont_days == 1:
    new_time = new_time + ' ' + '(' + 'next day' + ')'
  if cont_days > 1:
    new_time = new_time + ' ' + '(' + str(cont_days) + ' days later' + ')'


#  print(" ",
#        str(start_h).zfill(2), ':',
#        str(start_m).zfill(2), ' ',
#        str(start_AM_PH).zfill(2), ' ',
#        str(duration_h).zfill(2), ':',
#        str(duration_m).zfill(2), '  ', total, '    ', new_time)

  return new_time
