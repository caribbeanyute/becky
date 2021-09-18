#! /usr/bin/env python
 import os
port = int(os.environ['PORT']) if os.environ['PORT'] else 8084
from app import app
app.run(debug=True,host="0.0.0.0",port=port)
