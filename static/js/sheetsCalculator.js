const calculateRanks = (value, cost) => {
  let rank = document.getElementsByClassName(`rank${value}`);
  let rankStats = document.getElementsByClassName(`result${value}`);

  for (let i = 0; i < rank.length; i++) {
    let value = cost;
    for (let z = 1; z < rank[0].cells.length; z++) {
      if (rank[i].cells[z].children[0].value < 5) {
        value += rank[i].cells[z].children[0].value * 25;
      } else if (rank[i].cells[z].children[0].value >= 5) {
        value += rank[i].cells[z].children[0].value * 5;
      }
      rankStats[i].innerHTML = value;      
    }
  }
};

const calculateTotal = () => {
  let rank1 = document.getElementsByClassName("result1");
  let rank2 = document.getElementsByClassName("result2");
  let rank3 = document.getElementsByClassName("result3");
  let rank4 = document.getElementsByClassName("result4");
  let rankTotal = document.getElementsByClassName(`result5`);
  for (let i = 0; i < rankTotal.length; i++) {
    rankTotal[i].innerHTML =
      Number(rank1[i].innerHTML) +
      Number(rank2[i].innerHTML) +
      Number(rank3[i].innerHTML) +
      Number(rank4[i].innerHTML);
  }
};

calculateRanks(1, 75);
calculateRanks(2, 125);
calculateRanks(3, 125);
calculateRanks(4, 100);
calculateTotal();
