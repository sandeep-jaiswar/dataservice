# BUILD file for the data-ingestion-service

load("@rules_python//python/defs:build_defs.bzl", "py_library", "py_binary", "py_test") # Updated load path
load("@python_deps//:requirements.bzl", "requirement") # Updated load path to use the pip extension name

# Basic Python library rule for the service logic
py_library(
    name = "data-ingestion-service-lib",
    srcs = glob(["src/main/python/**/*.py"]),
    deps = [
        requirement("requests"),
        "//pkgs/data_models",
        "//pkgs/database_client",
    ],
)

# Example for a binary that runs the service
py_binary(
    name = "data-ingestion-service",
    srcs = ["src/main/python/main.py"],
    deps = [
        ":data-ingestion-service-lib",
    ],
    data = ["historical_data_sample.json"],
)

# === Formatting (Black) ===
# Load black from the python_deps module
load("@python_deps//:black.bzl", "black_fmt") # Updated load path

black_fmt(
    name = "format",
    srcs = glob(["src/main/python/**/*.py"]),
)

# === Linting (Flake8) ===
# Load flake8 from the python_deps module
load("@python_deps//:flake8.bzl", "flake8_test") # Updated load path

flake8_test(
    name = "lint",
    srcs = glob(["src/main/python/**/*.py"]),
)

# === Testing ===
py_test(
    name = "nse_symbols_test",
    srcs = ["src/test/python/test_nse_symbols.py"],
    deps = [
        ":data-ingestion-service-lib",
        "//pkgs/data_models",
    ],
)

py_test(
    name = "historical_data_fetcher_test",
    srcs = ["src/test/python/test_historical_data_fetcher.py"],
    deps = [
        ":data-ingestion-service-lib",
        "//pkgs/data_models",
    ],
    data = ["historical_data_sample.json"],
)

py_test(
    name = "data_ingestion_database_integration_test",
    srcs = ["src/test/python/integration_test.py"],
    deps = [
        ":data-ingestion-service-lib",
        "//pkgs/database_client",
        "//pkgs/data_models",
    ],
    data = ["historical_data_sample.json"],
)
