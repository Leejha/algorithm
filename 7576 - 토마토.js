const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
const [M, N] = input.shift().split(" ").map(Number);

const dx = [-1, 1, 0, 0];
const dy = [0, 0, -1, 1];

const graph = input.map((tomato) => tomato.split(" ").map(Number));

const queue = [];

for (let [rowIndex, rowTomatos] of graph.entries()) {
  for (let [tomatoIndex, tomato] of rowTomatos.entries()) {
    if (tomato === 1) {
      queue.push([rowIndex, tomatoIndex]);
    }
  }
}

for (let [x, y] of queue) {
  for (let i = 0; i < dx.length; i++) {
    let nx = x + dx[i];
    let ny = y + dy[i];

    if (nx >= 0 && nx < N && ny >= 0 && ny < M && graph[nx][ny] === 0) {
      graph[nx][ny] = graph[x][y] + 1;
      queue.push([nx, ny]);
    }
  }
}

let maxDay = 0;

for (let rowTomatos of graph) {
  for (let tomato of rowTomatos) {
    if (tomato === 0) {
      console.log(-1);
      return;
    }
    maxDay = Math.max(maxDay, tomato);
  }
}

console.log(maxDay - 1);
