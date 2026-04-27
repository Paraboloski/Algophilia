ifneq (,$(wildcard ./.env))
	include .env
	export
endif

.PHONY: main android

main:
	@uv sync
	@uv run main.py

android:
	@uv sync
	@uv run flet run main.py --android