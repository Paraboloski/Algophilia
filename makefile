ifneq (,$(wildcard ./.env))
	include .env
	export
endif

.PHONY: android

android:
	@uv sync
	@uv run flet run main.py --android