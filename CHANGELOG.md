# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

- Add GitHub Action to push package to PyPi

## [0.3.0] - 2023-01-13

### Added

- A little context awareness when working with services running in Nomad.
  - Example, `ServiceHealth` now has the `alloc_id` property

### Changed

- Limiting usage of imports from `typing`
  - For example, moving more hinting of lists from `List` to `list`

### Internal

- Added `Makefile` to make a few things easier to call all the time.

## [0.2.0] - 2022-10-27

### Added

- `/health/service/:service` support with model based return
- Tracing decorator for each endpoint call for basic span generation
- `timeout` option to the base `ConsulAPI` class to ensure we have a default timeout
  set but allow it to be overriden.


## [0.1.0] - 2022-10-24

### Changed

- Switched how we parse env vars for the following:
  - `CONSUL_HTTP_ADDR`
  - `CONSUL_HTTT_TOKEN`
  - `CONSUL_NAMESPACE`
  - 

### Added

- `/catalog/services` support with a basic example


