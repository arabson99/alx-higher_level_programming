#!/usr/bin/node

const count = 0;
exports.logMe = function (item) {
  console.log(`${count++}: ${item}`);
};
