#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let ans = 0;
  for (const i of list) {
    if (i === searchElement) {
      ans++;
    }
  }
  return ans;
};
