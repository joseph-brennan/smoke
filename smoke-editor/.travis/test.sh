#!/bin/bash
yarn global add codecov
yarn
yarn unit # should eventually be `yarn test`
codecov || true # for local tests
