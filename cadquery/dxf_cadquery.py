#!/usr/bin/env python3
import sys
import cadquery as cq

result = (
    cq.importers.importDXF(sys.argv[1]).wire().toPending()
)
