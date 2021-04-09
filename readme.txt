Super Random, Copyright TFB 2021.

Relies on : The Python "time" module.

feed_the_seed(seed) updates the random seed used <default="1234">.

super_random(r=0) returns a number between 0 and .9, (or r inclusive where r is a positive integer,) and lets the nanosecond timer change.  This is slower but better for larger quantities of random data generation.

super_fast_random(r=0) returns a number between 0 and .9 (or r inclusivewhere r is a positive integer.)  This is quicker than super_random() but it runs too quickly for repeated sequential requests as the time will be the same, generating similar numbers until a nanosecond passes.

Both super_random() and super_fast_random() generate a new 4 digit seed on each pass so you would need to catch and re-feed your seed to keep using it.