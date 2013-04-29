if [ -z "$BASH_SOURCE" ]; then
    echo "This script is meant to be sourced."
    exit 255
fi

SCRIPT=`readlink -f $BASH_SOURCE`
HERE=`dirname $SCRIPT`

export TOP=$HERE
# TODO: Make this more robust. What if it's already in the path?
if [ -z "$PATH" ]; then
    export PATH="$TOP/bin"
else
    export PATH="$TOP/bin:$PATH"
fi
