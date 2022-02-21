# bin/bash

for f in ./*.jpeg; do
    # do some stuff here with "$f"
    # remember to quote it or spaces may misbehave
    convert $f.jpeg -quality 40% $f-thumnail.jpeg
done 