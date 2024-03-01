build-archive:
	python3 dump_models.py
	./scripts/create-archives.sh

build-docker:
	podman build -t torchserve-all-minilm-l6-v2 .

serve: build-archive
	bash ./scripts/start-torchserve.sh


.PHONY: test