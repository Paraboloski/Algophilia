ifneq (,$(wildcard ./.env))
	include .env
	export
endif

push:
	@cmd /c cmd\push.bat

web:
	@cmd /c cmd\web.bat

android:
	@cmd /c cmd\android.bat

.PHONY: push web android