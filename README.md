# OneHourWindows
This Automation will only update exported csv files, applied to following delivery method. After updating, the csv file will have more rows than initial file, which one row represent one hour window. The bulk upload operation is still to be done manually.
- pickup
- drive up

Fields need to be update at csv files:
- Start Time
- End Time
- Pickup Time

Limite.g. The typical initial Start time is 11am, and End Time is 16am. After update the start time will be 11am, the end time will be 12pm (the first row), the start time will be 12pm, and end time will be 13pm (the second row).....The pickup time will be 1 min increments at each row.Please take a look at the example at the attachment for more details.
