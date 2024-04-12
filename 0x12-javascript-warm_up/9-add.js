#!/usr/bin/node
function add (a, b) {
  return a + b;
}
const x = process.argv[2]; const y = process.argv[3];
if (x === undefined || isNaN(x) || y === undefined || isNaN(y)) {
  console.log('NaN');
} else {
  console.log(add(parseInt(x), parseInt(y)));
}
