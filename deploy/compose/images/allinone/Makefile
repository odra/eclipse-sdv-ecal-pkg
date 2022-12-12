SHELL := /bin/bash

REG := quay.io
ORG := lrossett
NAME := ecal-cpp-allinone
TAG := latest-f37
IMAGE := ${REG}/${ORG}/${NAME}:${TAG}
CRIO := podman

image/build:
	${CRIO} build -t ${IMAGE} .

image/push:
	${CRIO} push ${IMAGE}

image/debug:
	${CRIO} run -it --entrypoint /bin/bash ${IMAGE}

.PHONY: image/build image/push image/debug
