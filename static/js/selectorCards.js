let cardToggle = false;
let cardCount = 0;
let cardPayload = []
let cardList = document.getElementById("cards-list");

axios.get(`${window.location.origin}/api/fiches/`).then(function (response) {
  cards = response.data;
  cardList.innerHTML = "";
  for (let i = 0; i < cards.length; i++) {
    cardList.innerHTML += `<div class="card-search-content-item"><input type="checkbox" onchange="handleCardCheck(event)" value="${cards[i].name}" name="card-request" /><label for="${cards[i].name}" class="card-search-content-item-label" onclick="handleCardClick(event)">${cards[i].name}</label></div>`;
  }
});

const handleCardPayload = () => {
  for (let i in cardPayload) {
    cardList.innerHTML += `<input type="text" name="send-card" value="${cardPayload[i]}" style="display: none" />`
  }
};

function panelCardToggle() {
  if (cardToggle == false) {
    cardToggle = true;
    $("#cards-selector-container").css("min-height", "315px");
    $("#cards-search-container").css("height", "235px");
    $("#cards-search-container").css("padding", "5px 0");
    $("#cards-search-container").css("border", "1px solid #938471");
    $(".card-search-content").css("height", "180px");
    $(".card-arrow").css("transform", "rotate(-90deg)");
    $(".cards-search-btn").css("display", "flex");
  } else {
    cardToggle = false;
    $("#cards-selector-container").css("min-height", "200px");
    $("#cards-search-container").css("height", "0px");
    $("#cards-search-container").css("padding", "0");
    $("#cards-search-container").css("border-top", "none");
    $("#cards-search-container").css("border-bottom", "none");
    $(".card-search-content").css("height", "0px");
    $(".card-arrow").css("transform", "rotate(90deg)");
    $(".cards-search-btn").css("display", "none");
  }
}

const handleCardClick = (event) => {
  event.target.closest("div").children[0].click();
};

const handleCardCheck = (event) => {
  if (event.target.checked) {
    cardCount += 1;
    cardPayload.push(event.target.value)
  } else {
    cardCount -= 1;
    for (let i in cardPayload) {
      if (cardPayload[i] == event.target.value) {
        cardPayload.splice(i, 1);
      }
    }
  }

  document.getElementById("card-selector-title").innerHTML =
    cardCount < 1
      ? "Ajouter une nouvelle carte"
      : cardCount == 1
      ? `${cardCount} carte sélectionnée`
      : `${cardCount} cartes sélectionnées`;
};

let cardResult = document.getElementById("card_search_bar_input");
cardResult.addEventListener("keyup", () => {
  let query = cardResult.value;
  cardList.innerHTML = "";
  let cardsList = cards.filter(function (card) {
    return card.name.toLowerCase().includes(query?.toLowerCase());
  });

  cardsList.map((card) => {
    return (cardList.innerHTML += `<div class="card-search-content-item"><input type="checkbox" onchange="handleCardCheck(event)" value="${card.name}" name="card-request" /><label for="${card.name}" class="card-search-content-item-label" onclick="handleCardClick(event)">${card.name}</label></div>`);
  });
});
