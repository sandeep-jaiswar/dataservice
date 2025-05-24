# BUILD file for the database-service

load("@rules_jvm//java:defs.bzl", "java_library", "java_binary")
load("@maven//:defs.bzl", "artifact")
load("@rules_jvm//java/toolchains:def.bzl", "java_toolchain_suite")

# Basic Java library rule
java_library(
    name = "database-service-lib",
    srcs = glob(["src/main/java/**/*.java"]),
    deps = [
        artifact("org.liquibase:liquibase-core"),
        artifact("org.postgresql:postgresql"),
        # Add any other internal dependencies here, e.g., from pkgs
    ],
    # If you have resources like Liquibase changelogs, you can add them here
    # resources = glob(["src/main/resources/**/*"]),
)

# Example for a binary that runs the service
# java_binary(
#     name = "database-service",
#     runtime_deps = [":database-service-lib"],
#     main_class = "com.yourcompany.databaseservice.Main", # Replace with your main class
# )

# === Formatting (Spotless with Google Java Format) ===
# This target can be run to format Java files in this directory
load("@rules_jvm//java/fmt:spotless.bzl", "spotless_java_fmt")

spotless_java_fmt(
    name = "format",
    srcs = glob(["src/main/java/**/*.java"]),
    # Referencing the formatter and dependencies from maven_install
    formatter = artifact("com.google.googlejavaformat:google-java-format"),
    deps = [
        artifact("com.diffplug.spotless:spotless-plugin-maven"),
    ],
)

# === Linting (Checkstyle) ===
# This target can be run to lint Java files in this directory
load("@rules_jvm//java/lint:checkstyle.bzl", "checkstyle_java_lint")

checkstyle_java_lint(
    name = "lint",
    srcs = glob(["src/main/java/**/*.java"]),
    # Referencing Checkstyle from maven_install
    checkstyle = artifact("com.puppycrawl.tools:checkstyle"),
    # You'll likely want a Checkstyle configuration file
    # config = "//:google_checks.xml", # Example, you'll need to create this
)
