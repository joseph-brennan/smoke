#!/bin/bash
export PATH="${PATH}:${HOME}/.local/bin"
pushd $(dirname $0)/..

# make sure failing tests cause failing
set -e
for part in smoke-editor smoke-backend smokr; do
    pushd ${part}
    [ -f .travis/test.sh ] && .travis/test.sh
    popd
done
set +e

popd
