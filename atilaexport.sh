#!/bin/bash
mongoexport --host localhost:27018 --db atila --collection registration --csv --out atila.csv --fields name,email,affiliation,Day1,Day2,Dinner,hotel,room,roommate,diet
