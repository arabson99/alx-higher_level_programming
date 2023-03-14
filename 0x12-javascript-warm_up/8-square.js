#!/usr/bin/node

const value = parseInt(process.argv[2]);

if (isNaN(value)) {
  console.log('Missing size');
} else if (value > 0) {
  let string = '';
  for (let i = 0; i < value; i++) {
    for (let j = 0; j < value; j++) {
      string += 'X';
    }
    string += '\n';
  }
  console.log(string);
}
