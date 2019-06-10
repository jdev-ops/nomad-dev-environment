FROM centos:centos7.6.1810

ENV LANG C.UTF-8

COPY ["./packages/jdk-11.x", "/usr/lib/jvm/" ]

# add a simple script that can auto-detect the appropriate JAVA_HOME value
# based on whether the JDK or only the JRE is installed
#RUN chmod +x /usr/lib/jvm/bin/java

ENV JAVA_HOME /usr/lib/jvm

ENV JAVA_VERSION 11u03

#RUN set -x && apt-get update && rm -rf /var/lib/apt/lists/*

RUN update-alternatives --install "/usr/bin/java" "java" "/usr/lib/jvm/bin/java" 2
RUN update-alternatives --install "/usr/bin/javac" "javac" "/usr/lib/jvm/bin/javac" 2
#RUN update-alternatives --config java
