import math, secrets, binascii
from collections import Counter

def eta(data, unit='natural'):
    base = {
        'shannon' : 2.,
        'natural' : math.exp(1),
        'hartley' : 10.
    }

    if len(data) <= 1:
        return 0

    counts = Counter()

    for d in data:
        counts[d] += 1

    ent = 0

    probs = [float(c) / len(data) for c in counts.values()]
    for p in probs:
        if p > 0.:
            ent -= p * math.log(p, base[unit])

    return ent

y = 0.0
i = 0
# Note: we don't need to do it all the way up to 5.5362 or so. We can do a simple ls on the output directory and that will be fine.
# This is so I can have an abundance of less random albeit easier to generate data.   
while y < 5.535:
	z = secrets.token_bytes(8192)
	Z = binascii.hexlify(z)
	y = eta(z)
#	if (i % 250) == 0:	print(i)
	i += 1

fd = open("entropy.out", "wb")
fd.write(z)
fd.close()
print(eta(z))
print(i)
