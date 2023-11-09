
import base64

steps = ["plan", "code", "test", "delivery", "deploy", "monitor"]

for step in steps:
    step_bytes = step.encode('utf-8')
    data = base64.b64encode(step_bytes)

    step_base64 = repr(data)
    print(step_base64)