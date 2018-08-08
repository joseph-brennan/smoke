#!/bin/bash
npm install -g codecov
yarn unit # should eventually be `yarn test`
codecov || true # for local tests
