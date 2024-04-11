#!/usr/bin/node
const x = process.argv[2];
if (x === undefined || isNaN(x)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < x; i++) {
    for (let j = 0; j < x; j++) {
      console.log('X');
    }
  }
}
