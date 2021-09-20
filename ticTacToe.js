var tictactoe = function (moves) {
  let player = 1;
  const rows = Array(3).fill(0);
  const cols = Array(3).fill(0);
  let diag = 0, anti_diag = 0;

  for (let i = 0; i < moves.length; i++) {
    rows[moves[i][0]] += player;
    cols[moves[i][1]] += player;

    if (moves[i][0] === moves[i][1]) {
      diag += player;
    }
    if (moves[i][0] + moves[i][1] === 2) {
      anti_diag += player;
    }

    if (Math.abs(rows[moves[i][0]]) === 3 || Math.abs(cols[moves[i][1]]) === 3 || Math.abs(diag) === 3 || Math.abs(anti_diag) === 3) {
      return player === 1 ? "A" : "B";
    }
    player *= -1;
  }

  return moves.length === 9 ? "Draw" : "Pending"
};

console.log(tictactoe([[0, 0], [2, 0], [1, 1], [2, 1], [2, 2]]));
console.log(tictactoe([[0, 0], [1, 1], [0, 1], [0, 2], [1, 0], [2, 0]]));
console.log(tictactoe([[0, 0], [1, 1], [2, 0], [1, 0], [1, 2], [2, 1], [0, 1], [0, 2], [2, 2]]));
console.log(tictactoe([[0, 0], [1, 1]]));
