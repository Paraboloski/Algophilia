ifneq (,$(wildcard ./.env))
	include .env
	export
endif

push:
	@cmd /c cmd\push.bat

dev:
	@cmd /c cmd\dev.bat

.PHONY: push dev