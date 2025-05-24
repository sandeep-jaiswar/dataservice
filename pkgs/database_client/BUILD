# BUILD file for pkgs/database_client

load("@rules_python//python:defs.bzl", "py_library", "py_test")
load("@python_lint_deps//:requirements.bzl", "requirement")

py_library(
    name = "database_client",
    srcs = glob(["src/main/python/**/*.py"]),
    deps = [
        "//pkgs/data_models", # Depends on the data models
        requirement("psycopg2-binary"), # Depends on psycopg2
    ],
    visibility = [
        "//services/data-ingestion-service:__subpackages__",
        "//services/data-processing-service:__subpackages__",
        "//apps/data_backfill_tool:__subpackages__",
        "//pkgs/database_client/src/test/python:__subpackages__",
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
    name = "database_client_test",
    srcs = ["src/test/python/test_database_client.py"],
    deps = [
        ":database_client", # The test depends on the database_client library
        # Mocking is part of standard Python libraries, so no extra deps needed for mock.
    ],
)
