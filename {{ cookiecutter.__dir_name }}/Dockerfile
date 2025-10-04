FROM debian:bookworm

ARG DEBIAN_DIST
ARG UPSTREAM_VERSION
ARG BUILD_VERSION
ARG FULL_VERSION
ARG ARCH
ARG UPSTREAM_RELEASE

RUN mkdir -p /output/usr/bin
RUN mkdir -p /output/usr/share/doc/{{ cookiecutter.__pkg_hyphen }}
RUN mkdir -p /output/DEBIAN

COPY ${UPSTREAM_RELEASE}/* /output/usr/bin/
COPY {{ cookiecutter.__pkg_hyphen }}-contents/DEBIAN/* /output/DEBIAN/
COPY {{ cookiecutter.__pkg_hyphen }}-contents/copyright /output/usr/share/doc/{{ cookiecutter.__pkg_hyphen }}/
COPY {{ cookiecutter.__pkg_hyphen }}-contents/changelog.Debian /output/usr/share/doc/{{ cookiecutter.__pkg_hyphen }}/
COPY {{ cookiecutter.__pkg_hyphen }}-contents/README.md /output/usr/share/doc/{{ cookiecutter.__pkg_hyphen }}/

RUN sed -i "s/DIST/$DEBIAN_DIST/" /output/usr/share/doc/{{ cookiecutter.__pkg_hyphen }}/changelog.Debian
RUN sed -i "s/FULL_VERSION/$FULL_VERSION/" /output/usr/share/doc/{{ cookiecutter.__pkg_hyphen }}/changelog.Debian
RUN sed -i "s/DIST/$DEBIAN_DIST/" /output/DEBIAN/control
RUN sed -i "s/UPSTREAM_VERSION/$UPSTREAM_VERSION/" /output/DEBIAN/control
RUN sed -i "s/BUILD_VERSION/$BUILD_VERSION/" /output/DEBIAN/control
RUN sed -i "s/SUPPORTED_ARCHITECTURES/$ARCH/" /output/DEBIAN/control

RUN dpkg-deb --build /output /{{ cookiecutter.__pkg_hyphen }}_${FULL_VERSION}.deb
