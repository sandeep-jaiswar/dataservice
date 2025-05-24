# BUILD file for pkgs/mypythonlib

load("@rules_python//python:defs.bzl", "py_library")
load("@python_lint_deps//:requirements.bzl", "requirement")

# Basic Python library rule (example)
py_library(
    name = "mypythonlib",
    srcs = glob(["**/*.py"]),
    # Add dependencies here if needed
)

# === Formatting (Black) ===
# This target can be run to format Python files in this directory
load("@python_lint_deps//:black.bzl", "black_fmt")

black_fmt(
    name = "format",
    srcs = glob(["**/*.py"]),
)

# === Linting (Flake8) ===
# This target can be run to lint Python files in this directory
load("@python_lint_deps//:flake8.bzl", "flake8_test") # flake8 is typically run as a test

flake8_test(
    name = "lint",
    srcs = glob(["**/*.py"]),
)
