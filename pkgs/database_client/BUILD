# BUILD file for pkgs/database_client

load("@rules_python//python/defs:build_defs.bzl", "py_library", "py_test") # Updated load path
load("@python_deps//:requirements.bzl", "requirement") # Updated load path to use the pip extension name

py_library(
    name = "database_client",
    srcs = glob(["src/main/python/**/*.py"]),
    deps = [
        "//pkgs/data_models",
        requirement("psycopg2-binary"),
    ],
    visibility = [
        "//services/data-ingestion-service:__subpackages__",
        "//services/data-processing-service:__subpackages__",
        "//apps/data_backfill_tool:__subpackages__",
        "//pkgs/database_client/src/test/python:__subpackages__",
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
    name = "database_client_test",
    srcs = ["src/test/python/test_database_client.py"],
    deps = [
        ":database_client",
    ],
)
