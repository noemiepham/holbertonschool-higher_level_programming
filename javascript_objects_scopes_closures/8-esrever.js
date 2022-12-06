#!/usr/bin/node

exports.esrever = function (list) {
  const table = [];
  for (let i = list.length - 1; i >= 0; i--) {
    table.push(list[i]);
  }
  return (table);
};
