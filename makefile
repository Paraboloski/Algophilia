ifneq (,$(wildcard ./.env))
	include .env
	export
endif

push:
	@call .venv\Scripts\activate && cmd /c cmd\push.bat

dev:
	@call .venv\Scripts\activate && cmd /c cmd\dev.bat

.PHONY: push dev