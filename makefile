ifneq (,$(wildcard ./.env))
	include .env
	export
endif

push:
	@cmd\push.bat

dev:
	@.venv\Scripts\python main.py

.PHONY: push dev