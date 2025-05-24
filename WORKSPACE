# This WORKSPACE file configures the external dependencies for your project.

# === Python Rules ===
load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

http_archive(
    name = "rules_python",
    sha256 = "857b26d6154038322621860a142b55365991133547f8532305a1ac2018a25218",
    strip_prefix = "rules_python-0.28.1",
    url = "https://github.com/bazelbuild/rules_python/releases/download/0.28.1/rules_python-0.28.1.tar.gz",
)

load("@rules_python//python:repositories.bzl", "python_register_toolchains", "pip_install")

python_register_toolchains(
    name = "python",
    python_version = "3.9",
)

# Install Black and Flake8 via pip
pip_install(
    name = "python_lint_deps",
    requirements = "//:requirements.txt", # We'll create this file next
    python_interpreter_target = "@python//:current_interpreter",
)

# === Java Rules ===
load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

http_archive(
    name = "rules_jvm_external",
    sha256 = "a87a00717741872f39045f6a30114406b1510ef8d52c10d37734397c7b09022a",
    strip_prefix = "rules_jvm_external-4.0",
    url = "https://github.com/rules-by-example/rules_jvm_external/releases/download/4.0/rules_jvm_external-4.0.tar.gz",
)

load("@rules_jvm_external//:defs.bzl", "maven_install")

maven_install(
    artifacts = [
        "org.liquibase:liquibase-core:4.24.0",
        "org.postgresql:postgresql:42.6.0",
        # Add Spotless and Checkstyle dependencies for rules_jvm
        "com.diffplug.spotless:spotless-plugin-maven:2.43.0", # Used by rules_jvm spotless rule
        "com.google.googlejavaformat:google-java-format:1.17.0", # Used by spotless
        "com.puppycrawl.tools:checkstyle:10.12.4", # Used by rules_jvm checkstyle rule
    ],
    repositories = [
        "https://repo1.maven.org/maven2",
    ],
    generate_compat_repositories = True,
)

# Fetch rules_jvm for better Java tooling integration (formatting, linting, etc.)
http_archive(
    name = "rules_jvm",
    sha256 = "4b5b6c013880324f7c5b475c2f934b2c8a424f4b3a2017b6a5e0c8a8e3a4d9e2", # Example SHA, check latest
    strip_prefix = "rules_jvm-0.0.6", # Example version, check latest
    url = "https://github.com/bazelbuild/rules_jvm/archive/refs/tags/0.0.6.tar.gz", # Example URL, check latest tag
)

load("@rules_jvm//java:defs.bzl", "java_binary", "java_library", "java_test", "java_library_suites", "java_binary_suites", "java_test_suites")

# === Formatting and Linting ===
# We will define targets for these in the BUILD files.

# === PostgreSQL ===
# Handled in BUILD files.
