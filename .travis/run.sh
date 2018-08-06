#!/bin/bash
# make sure failing tests cause failing

export PATH="${PATH}:${HOME}/.local/bin"
source smoke-env

for part in smoke-editor smoke-backend ; do
    pushd ${part}
    mkenv
    set -e
    [ -f .travis/test.sh ] && bash .travis/test.sh
    set +e
    unenv
    popd
done
