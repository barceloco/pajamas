#!/bin/bash

sphinx-apidoc -f -o . ../pajamas \
&& make clean html \
&& python -m http.server --directory _build/html/ 8000
