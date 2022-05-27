const calculateRanks = (index, cost) => {
  let rank = document.getElementsByClassName(`rank${index}`);
  let rankStats = document.getElementsByClassName(`result${index}`);
  let value = cost;
  for (let i = 1; i < rank[0].cells.length; i++) {
    
      if (rank[0].cells[i].children[0].value < 5) {
        value += (rank[0].cells[i].children[0].value * 25);
      } else if (rank[0].cells[i].children[0].value >= 5) {
        value += (rank[0].cells[i].children[0].value * 5);
      }
      rankStats[0].value = value;
  }
 
};

const calculateTotal = () => {
  let rank1 = document.getElementsByClassName("result1");
  let rank2 = document.getElementsByClassName("result2");
  let rank3 = document.getElementsByClassName("result3");
  let rank4 = document.getElementsByClassName("result4");
  let rankTotal = document.getElementsByClassName(`result5`);
  for (let i = 0; i < rankTotal.length; i++) {
    rankTotal[i].value =
      Number(rank1[i].value) +
      Number(rank2[i].value) +
      Number(rank3[i].value) +
      Number(rank4[i].value);
  }
};

calculateRanks(1, 75);
calculateRanks(2, 125);
calculateRanks(3, 125);
calculateRanks(4, 100);
calculateTotal();
