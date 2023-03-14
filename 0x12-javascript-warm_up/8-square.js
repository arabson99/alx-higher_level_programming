#!/usr/bin/node

const value = parseInt(process.argv[2]);

if (isNaN(value)) {
  console.log('Missing size');
} else if (value > 0) {
  for (let i = 0; i < value; i++) {
    let string = '';
    for (let j = 0; j < value; j++) {
      string += 'X';
    }
    console.log(string);
  }
}
