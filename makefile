ifneq (,$(wildcard ./.env))
	include .env
	export
endif

push:
	@ cmd\push.bat

.PHONY: push