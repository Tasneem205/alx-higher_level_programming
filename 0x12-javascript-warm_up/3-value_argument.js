#!/usr/bin/node
const v = process.argv.length;
if (v === 2) {
  console.log('No Argument');
} else if (v > 2) {
  console.log(process.argv[2]);
}
