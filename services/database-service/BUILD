# BUILD file for the database-service

load("@rules_jvm//java:defs.bzl", "java_library", "java_binary", "java_test") # Updated load path
load("@maven//:defs.bzl", "artifact") # Load artifact from the maven extension

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

# Example for a binary that runs the service (uncomment and configure when needed)
# java_binary(
#     name = "database-service",
#     runtime_deps = [":database-service-lib"],
#     main_class = "com.yourcompany.databaseservice.Main", # Replace with your main class
# )

# === Formatting (Spotless with Google Java Format) ===
load("@rules_jvm//java/fmt:spotless.bzl", "spotless_java_fmt") # Updated load path

spotless_java_fmt(
    name = "format",
    srcs = glob(["src/main/java/**/*.java"]),
    formatter = artifact("com.google.googlejavaformat:google-java-format"),
    deps = [
        artifact("com.diffplug.spotless:spotless-plugin-maven"),
    ],
)

# === Linting (Checkstyle) ===
load("@rules_jvm//java/lint:checkstyle.bzl", "checkstyle_java_lint") # Updated load path

checkstyle_java_lint(
    name = "lint",
    srcs = glob(["src/main/java/**/*.java"]),
    checkstyle = artifact("com.puppycrawl.tools:checkstyle"),
    config = artifact("com.puppycrawl.tools:checkstyle", path = "google_checks.xml"),
)

# === Testing ===
load("@rules_jvm//java:defs.bzl", "java_test") # Ensure java_test is loaded from rules_jvm

java_test(
    name = "database_service_test",
    srcs = glob(["src/test/java/**/*.java"]),
    deps = [
        ":database-service-lib",
        artifact("org.junit.jupiter:junit-jupiter-api"), # These dependencies are now fetched via Bzlmod/maven
        artifact("org.junit.jupiter:junit-jupiter-engine"),
    ],
    runtime_deps = [
        artifact("org.junit.platform:junit-platform-launcher"),
    ],
)
