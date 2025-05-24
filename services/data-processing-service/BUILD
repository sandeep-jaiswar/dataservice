# BUILD file for the data-processing-service

load("@rules_python//python/defs:build_defs.bzl", "py_library", "py_binary", "py_test") # Updated load path
load("@python_deps//:requirements.bzl", "requirement") # Updated load path

py_library(
    name = "data-processing-service-lib",
    srcs = glob(["src/main/python/**/*.py"]),
    deps = [
        "//pkgs/data_models",
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
load("@python_deps//:black.bzl", "black_fmt") # Updated load path

black_fmt(
    name = "format",
    srcs = glob(["src/main/python/**/*.py"]),
)

# === Linting (Flake8) ===
load("@python_deps//:flake8.bzl", "flake8_test") # Updated load path

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
        "//pkgs/data_models",
    ],
)
