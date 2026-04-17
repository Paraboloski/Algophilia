ifneq (,$(wildcard ./.env))
	include .env
	export
endif

push:
	@cmd\push.bat

dev-pc:
	@cmd\dev_win.bat

dev-apk:
	@cmd\dev_apk.bat

main:
	@.venv\Scripts\python main.py

.PHONY: push dev-apk dev-pc main