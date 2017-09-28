#!/bin/python3

import sys

S = input().strip()
try:
    S_int = int(S)
except ValueError:
    print('Bad String')
except NameError:
    print('Bad String')
except Exception:
    print('Bad String')  
finally:
    print(str(S_int))
