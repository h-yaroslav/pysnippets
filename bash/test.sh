#/bin/sh
# Show all the colors of the rainbow, should be run under bash
#Style           Foreground      Background
#1st Digit       2nd Digit       3rd Digit
#0 - Reset       30 - Black      40 - Black
#1 - FG Bright   31 - Red        41 - Red
#2 - Unknown     32 - Green      42 - Green
#3 - Unknown     33 - Yellow     43 - Yellow
#4 - Underline   34 - Blue       44 - Blue
#5 - BG Bright   35 - Magenta    45 - Magenta
#6 - Unknown     36 - Cyan       46 - Cyan
#7 - Reverse     37 - White      47 - White

# BG=5 is blinking
for STYLE in 0 1 2 3 4 6 7; do
  for FG in 30 31 32 33 34 35 36 37; do
      CTRL="\033[${STYLE};${FG}m"
      echo -en "${CTRL}"
      echo -n "${STYLE};${FG}"
      echo -en "\033[0m\t"
  done
  echo
done
# Reset
echo -e "\033[0m"
