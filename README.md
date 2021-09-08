SMART Health Card Reader
==

Simple python script which decodes the content of a SMART health card like the ones being rolled out as vaccine cards in
BC, Quebec and other jurisdictions.

Instructions
--

Read your smart health card using a generic QR code reader, this should show you a string something like:
```
shc:/01234567890123456789...
```

Copy the long string of decimal digits, and feed that to the python script on standard in.