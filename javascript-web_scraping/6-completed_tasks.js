#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const todos = JSON.parse(body);

    // Create an object to store the count of completed tasks for each user
    const completedTasksCount = {};

    // Iterate through the todos and count completed tasks for each user
    for (const todo of todos) {
      if (todo.completed) {
        if (completedTasksCount[todo.userId]) {
          completedTasksCount[todo.userId]++;
        } else {
          completedTasksCount[todo.userId] = 1;
        }
      }
    }

    // Print the user IDs and the number of completed tasks
    console.log(completedTasksCount);
  } else {
    console.error(error || `Failed to fetch data. Status code: ${response.statusCode}`);
  }
});
