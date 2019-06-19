#!/usr/bin/env bash

DATASET_ZIP=rosalind_datasets.zip
DATASET_LINK=https://www.dropbox.com/s/9tlg42vjby4pa6o/${DATASET_ZIP}

if [ ! -f dataset1 -o ! -f dataset2 -o ! -f dataset3 ]; then
    wget ${DATASET_LINK} &>setup.log && \
	unzip ${DATASET_ZIP} && \
	rm ${DATASET_ZIP}
else
    echo "Datasets already deflated"
fi
