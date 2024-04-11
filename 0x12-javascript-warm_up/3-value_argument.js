#!/usr/bin/node
const v = process.argv[2];
if (v === undefined) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
