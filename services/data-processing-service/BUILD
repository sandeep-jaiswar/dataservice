# BUILD file for the data-processing-service

load("@rules_python//python:defs.bzl", "py_library", "py_binary", "py_test")
load("@python_lint_deps//:requirements.bzl", "requirement")

py_library(
    name = "data-processing-service-lib",
    srcs = glob(["src/main/python/**/*.py"]),
    deps = [
        "//pkgs/data_models", # Depends on data models
        # Add other dependencies like pandas if used for processing
        # requirement("pandas"),
    ],
)

py_binary(
    name = "data-processing-service",
    srcs = ["src/main/python/main.py"],
    deps = [
        ":data-processing-service-lib",
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
    name = "data_processing_service_test",
    srcs = ["src/test/python/test_processor.py"],
    deps = [
        ":data-processing-service-lib",
        "//pkgs/data_models", # Tests also depend on data models
    ],
)
