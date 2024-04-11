#!/usr/bin/node
const v = process.argv[2];
if (v === undefined) {
  console.log('No Argument');
} else {
  console.log(process.argv[2]);
}
