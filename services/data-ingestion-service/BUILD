# BUILD file for the data-ingestion-service

load("@rules_python//python:defs.bzl", "py_library", "py_binary", "py_test")
load("@python_lint_deps//:requirements.bzl", "requirement")

# Basic Python library rule for the service logic
py_library(
    name = "data-ingestion-service-lib",
    srcs = glob(["src/main/python/**/*.py"]),
    deps = [
        # Add dependencies for HTTP requests (e.g., requests)
        requirement("requests"),
        # Add dependencies for data processing (e.g., pandas if needed)
        # requirement("pandas"),
        # Add any internal dependencies here, e.g., from pkgs
    ],
)

# Example for a binary that runs the service
py_binary(
    name = "data-ingestion-service",
    srcs = ["src/main/python/main.py"],
    deps = [
        ":data-ingestion-service-lib",
    ],
)

# === Formatting (Black) ===
load("@python_lint_deps//:black.bzl", "black_fmt")

black_fmt(
    name = "format",
    srcs = glob(["src/main/python/**/*.py"]),
)

# === Linting (Flake8) ===
load("@python_lint_deps//:flake8.bzl", "flake8_test")

flake8_test(
    name = "lint",
    srcs = glob(["src/main/python/**/*.py"]),
)

# === Testing ===
py_test(
    name = "nse_symbols_test",
    srcs = ["src/test/python/test_nse_symbols.py"],
    deps = [
        ":data-ingestion-service-lib", # The test depends on the library it's testing
    ],
)
