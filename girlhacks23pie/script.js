var task1 = "goal1"
var task2 = "goal2"
var task3 = "goal3"
var task4 = "goal4"
var task5 = "goal5"
var task6 = "goal6"

anychart.onDocumentReady(function() {

  // set the data
  var data = [
    { x: task1, value: 223553265 },
    { x: task2, value: 38929319 },
    { x: task3, value: 2932248 },
    { x: task4, value: 14674252 },
    { x: task5, value: 540013 },
    { x: task6, value: 19107368 }
  ];

  // create the chart
  var chart = anychart.pie();

  // set the chart title
  chart.title("Time Dedicated To Tasks");

  // add the data
  chart.data(data);

  // display the chart in the container
  chart.container('container');
  chart.draw();

});

var holder = 0;

function one() {
  document.getElementById("main_txt").innerHTML = "Goal #1";
  holder = 1;
  
}

function two() {
  document.getElementById("main_txt").innerHTML = "Goal #1";
  holder = 2;
}

function three() {
  document.getElementById("main_txt").innerHTML = "Goal #3";
  holder = 3;
}

function four() {
  document.getElementById("main_txt").innerHTML = "Goal #4";
  holder = 4;
}

function five() {
  document.getElementById("main_txt").innerHTML = "Goal #5";
  holder = 5;
}

function six() {
  document.getElementById("main_txt").innerHTML = "Goal #6";
  holder = 6;
}

function formdata() {
  const input = document.getElementById("name");
  if (holder == 1) {
    task1 = input.value;
    console.log(input.value);
  }
}