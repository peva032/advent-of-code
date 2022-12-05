#!/usr/bin/env bash

# Handling input args
for i in "$@"; do
    case $i in
        -d=*|--day=*)
            DAY="${i#*=}"
            shift
            ;;
        -*|--*)
            echo "Unknown argument $i"
            exit 1
            ;;
        *)
            ;;
    esac
done

INPUT_DATA_URL="https://adventofcode.com/${YEAR}/day/${DAY}/input"
YEAR=2022
DAY="$(printf %02d ${DAY})"
WORD_YEAR=twenty_twentytwo
INPUT_DATA_PATH="${PWD}/advent_of_code/data/${YEAR}"
PROBLEM_PATH="${PWD}/advent_of_code/problems/${WORD_YEAR}"
TESTS_PATH="${PWD}/tests/problems/${WORD_YEAR}"

INPUT_DATA_FILE="${INPUT_DATA_PATH}/input_${DAY}.txt"
PROBLEM_FILE="${PROBLEM_PATH}/day_${DAY}.py"
TEST_FILE="${TESTS_PATH}/test_day_${DAY}.py"
    

echo "Creating input data file: ${INPUT_DATA_FILE}"
if [ ! -f $INPUT_DATA_FILE ]; then
    touch $INPUT_DATA_FILE
else
    echo "Skipped! File already exists"
fi

echo "Creating problem Python file: ${PROBLEM_FILE}"
if [ ! -f $PROBLEM_FILE ]; then
    touch $PROBLEM_FILE
    echo "from advent_of_code.utils import get_input_data" >> $PROBLEM_FILE
else
    echo "Skipped! File already exists"
fi

echo "Creating test file: ${TEST_FILE}"
if [ ! -f $TEST_FILE ]; then
    touch $TEST_FILE
    echo "import pytest" >> $TEST_FILE
else
    echo "Skipped! File already exists"
fi