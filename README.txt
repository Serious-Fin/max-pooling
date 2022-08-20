Why write this project?

Heard about this technique called "max-pooling" in AI image processing and was curious about the results.

What's "Max-Pooling"?

Algorithm, that takes a *pool* of pixels, finds the brightest one (highest sum of rgb values) and replaces *pool* with single pixel.

Why use it?

This way of processing an image helps to reduce the amount of unnecessary detail (hence faster to work with later) while preserving overall shapes.

Why did you use X when Y is slightly faster?

Project was written as a test in Python just to get an idea of how an image looks with various size pools. If it were to be used in an actual AI, this algorithm should be rewritten in a diiferent language and optimized.

How to use it?

Command-line argument:
- python pooling.py input.jpg 4
Last number is what pool size you want (eg. 4x4) 