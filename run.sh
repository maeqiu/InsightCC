#!/bin/sh
#shell script to execute the code for both features
#input directory: tweet_input
#output directory: tweet_output

echo "Starting..."
echo "Running the 1st feature, output to tweet_output/ft1.txt"
python ./src/words_tweeted.py ./tweet_input/tweets.txt ./tweet_output/ft1.txt

echo "Running the 2nd feature, output to tweet_output/ft2.txt"
python ./src/median_unique.py ./tweet_input/tweets.txt ./tweet_output/ft2.txt

echo "Done!"
