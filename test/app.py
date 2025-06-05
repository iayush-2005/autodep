import os
import sys
import requests   # ✅ 3rd-party
import numpy       # ✅ 3rd-party
import helpers     # ✅ local module (from utils)
import fake_module # ❌ should trigger as missing
