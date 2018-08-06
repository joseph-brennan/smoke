#!/bin/bash

yarn unit # should eventually be `yarn test`
(cd ../ && cat smoke-editor/test/unit/coverage/lcov.info | node smoke-editor/node_modules/coveralls/bin/coveralls.js) || true # for local tests
