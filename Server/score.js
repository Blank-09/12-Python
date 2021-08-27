// https://github.com/Blank-09/12-Python/tree/main/Server
const author = "Priyanshu";

// update(50, [8, 14])
// update(50, [23, 8, 14, 27])
// update(50, [27, 8, 27, 23])
// update(50, [27, 14, 8])
// update(50, [27, 14])
// update(100, [23,  27])
// update(100, [27, 14])
// update(100,[8, 23, 27])
// update(100,[23, 14, 27])
// update(100, [27, 8])

const points = ``;

// Parser
points.trim().split("\n").forEach((line) => {
  if (line != "") {
    let quePoints = line;
    quePoints = quePoints.split(":");
    update(quePoints[0].trim(), quePoints[1].trim().split(" "));
  }
});


