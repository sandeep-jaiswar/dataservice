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
        "//pkgs/data_models", # Depends on the data models
        "//pkgs/database_client", # Depends on the database client
    ],
)

# Example for a binary that runs the service
py_binary(
    name = "data-ingestion-service",
    srcs = ["src/main/python/main.py"],
    deps = [
        ":data-ingestion-service-lib",
    ],
    data = ["historical_data_sample.json"], # Add the JSON file as a data dependency
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
    data = ["historical_data_sample.json"], # The test also needs the JSON file
)

py_test(
    name = "data_ingestion_database_integration_test",
    srcs = ["src/test/python/integration_test.py"],
    deps = [
        ":data-ingestion-service-lib",
        "//pkgs/database_client", # Depends on the database client
        "//pkgs/data_models", # Depends on data models
    ],
    data = ["historical_data_sample.json"], # The test needs the JSON file
)
