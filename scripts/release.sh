#!/bin/sh
set -e

binary_path=basm.bin
cargo +nightly build --release "$@"
python3 scripts/remove-got.py -o no-got target/x86_64-unknown-linux-gnu/release/basm
objcopy --strip-unneeded -j .init -j .text -j .rodata -O binary no-got $binary_path

basename=$(basename $0)
show_original=1
if [ "$basename" = 'release-asm.sh' ]; then
    ext=asm
    show_original=0
elif [ "$basename" = 'release-rs.sh' ]; then
    ext=rs
else
    ext=c
fi
template_path=scripts/template.$ext
python3 scripts/gen.py $binary_path $template_path $show_original
