# BUILD file for pkgs/data_models

load("@rules_python//python:defs.bzl", "py_library", "py_test")

py_library(
    name = "data_models",
    srcs = glob(["**/*.py"]),
    visibility = [
        "//services/data-ingestion-service:__subpackages__",
        "//services/data-processing-service:__subpackages__",
        "//apps/data_backfill_tool:__subpackages__",
    ], 
    # Add dependencies if the models depend on other libraries
)

py_test(
    name = "data_models_test",
    srcs = ["src/test/python/test_models.py"],
    deps = [
        ":data_models", # The test depends on the data_models library
    ],
)
