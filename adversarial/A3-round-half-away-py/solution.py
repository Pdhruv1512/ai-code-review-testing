import sys
from decimal import Decimal, ROUND_HALF_UP

for line in sys.stdin:
    line = line.strip()
    if line:
        number = Decimal(line)
        result = number.quantize(Decimal("1"), rounding=ROUND_HALF_UP)
        print(int(result))
