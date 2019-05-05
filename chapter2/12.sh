#!/usr/bin/env bash
head -n 1 $1 > col1.txt
head -n 2 $1 | tail -n 1 > col2.txt