# BK894-895-LCR-Meter-USB
Simple Python script for BK894 &amp; BK895 Bench LCR meters.
For more details and to modify this code, look at the [programming manual] bellow....

- select device
- start/target value, step value --> creates an array
  (ex. start = -5.0V, target = 5.0V, step = 0.1V
--> [-5.0, -4.9 ... 4.9, 5.0, 4.9 ...-5.0]
- select measurement type
- set Frequency
- save to .csv

Manual: https://bkpmedia.s3.amazonaws.com/downloads/manuals/en-us/894_895_manual.pdf
Programming Manual: https://bkpmedia.s3.amazonaws.com/downloads/programming_manuals/en-us/894_895_programming_manual.pdf
Datasheet: https://bkpmedia.s3.amazonaws.com/downloads/datasheets/en-us/894_895_datasheet.pdf
