#!/usr/bin/node
function fact (a) {
  if (a === 1) { return 1; }
  return a * fact(a - 1);
}
const x = process.argv[2];
if (x === undefined || isNaN(x)) {
  console.log('1');
} else {
  console.log(fact(parseInt(x)));
}
