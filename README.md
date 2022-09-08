# pyconsul

API client for [HashiCorp Consul](https://www.consul.io).

# Background

Main two motivations behind this project:

- Create a Python API client for Consul that returned typed responses via
  models (Pydantic model objects or at least Python data classes).
- Learn about creating and maintaining an OSS project.
- Create a client library that supported OpenTelemetry.

At work we make use of the entire Hashi stack (Consul, Nomad, Vault, etc) and
for some of our projects, we're split between Go and Python. Most of the Python
clients that exist today didn't seem to fit the need that we had.

That and we've heavily invested into OpenTelemetry, which is something that seems
to be lacking in a number of projects. If it wasn't for the desire that I had
to return typed objects, I'd likely have looked to contribute to the other
existing projects.
