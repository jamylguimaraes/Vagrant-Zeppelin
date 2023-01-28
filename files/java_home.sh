#!/usr/bin/env bash
# Set JDK installation directory according to selected Java compiler

export JAVA_HOME=$(readlink -f /usr/bin/java | sed "s:/bin/java::")
