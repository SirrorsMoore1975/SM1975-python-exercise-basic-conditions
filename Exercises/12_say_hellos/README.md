# say_hellos

This question is an advanced question and may required deeper understanding on the Python programming

## Introduction

There are approximately 192 known countries, each of which might have their own language / dialect or similar languages to speak within a region to one another. And that, we have approximately 31,000 languages and about 7,000 of the language that we are still speaking them [^1] [^2] . When you want a software that can be accessed to most of the people on this planet, your software might needed to be able to communicate with those users who speak in a different language. This `say_hellos` exercise is intended to give you a feel how it might be like to write a script that involved so many different language all at once.

## Pre-requirement

For this exercise you needed to know the following:

- How to write `Classes` in Python
- How to interact with a `json` file in Python

## Task

You task is to write a class that can handle:

### the `hellos` languages

- to handle add / remove `hellos` language
- to handle change / amended the `hellos` of a given language, so that changes do reflected upon greeting the person
- to allow a particular `hellos` language to reset to its default value
- to allow all `hellos` languages to reset to its default value

### the age limit

- to check the age limit of that particular language speaker
- to use given age property to see if this person is at the age limit or above (i.e. the default age, `20`, to became an adult)
- to have a function that can alter the age limit
- to have a function to alter a particular languages speaker age limit
- to allow reset to default age limit for a particular language
- to allow age limited to reset to the default value, i.e. 20

### the consolidate function

- handle greeting to a given user, where a data of users are given which containing their names, age, and language they speaks
- handle cases when the language does not show up
- read to a `json` file, and will not alter the content of the given `json` file, this `json` file data should be consider the language default
- handle a full reset function so that the `hellos` language, age limit return to its default value

Follow the given test lay down in the `test_scripts.py` and write to the `scripts.py` and `greetings.py` so that all tests are passed.

## Sources

[How to Say How are you in 50 Different Language](https://lingo-apps.com/say-how-are-you-in-different-languages/)

[How are you 70 different languages](https://lexiglobe.com/how-are-you-70-different-languages/)

## References

[^1] : [University of Huston: The Language Death](https://engines.egr.uh.edu/episode/2723) By Richard Armstrong

[^2] : [BBC: Language of the World](https://www.bbc.co.uk/languages/guide/languages.shtml)
