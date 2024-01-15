# Builder image
FROM ghcr.io/alexgseymour/torch-serve-arm64:latest AS builder

WORKDIR /usr/app
ADD requirements.txt .
RUN pip install -r requirements.txt

ADD dump_models.py .
RUN python dump_models.py

ADD handlers/cross_encoder/handler.py handlers/cross_encoder/handler.py
ADD handlers/embedding/handler.py handlers/embedding/handler.py

ADD scripts/create-archives.sh scripts/create-archives.sh

RUN ./scripts/create-archives.sh

# Production image
FROM ghcr.io/alexgseymour/torch-serve-arm64:latest

ADD requirements.txt .
RUN pip install -r requirements.txt

ADD docker/entrypoint.sh entrypoint.sh
ADD scripts/start-torchserve.sh start-torchserve.sh

COPY --from=builder /usr/app/model_store model_store

ENTRYPOINT [ "./entrypoint.sh" ]

CMD ["./start-torchserve.sh"]