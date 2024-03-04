#!/bin/bash

# --ncs means the snapshot feature is disabled.

echo "server is starting..."
torchserve --foreground --model-store model_store --models embedder=multilingual-e5-small.mar,cross_encoder=mmarco-mMiniLMv2-L12-H384-v1.mar --ncs