#!/bin/bash
yarn global add codecov
yarn
yarn unit && (codecov || true) # for local tests
