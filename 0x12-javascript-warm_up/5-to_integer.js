#!/usr/bin/node
const x = process.argv[2];
if (x === undefined || isNaN(x)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parseInt(x));
}
