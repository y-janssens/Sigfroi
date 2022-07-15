let queryToggle = false;
let queryCount = 0;
let queryPayload = [];
let queryList = document.getElementById(`${query}s-list`);

window.onload = parse(queryParse);

function parse(querysList) {
  querysList.map((item) => {
    return (queryList.innerHTML += `<div class="${query}-search-content-item"><input type="checkbox" onchange="handleQueryCheck(event)" value="${item.name}" name="${item}-request" /><label for="${item.name}" class="${item}-search-content-item-label" onclick="handleQueryClick(event)">${item.name}</label></div>`);
  });
}

let queryResult = document.getElementById(`${query}_search_bar_input`);
queryResult.addEventListener("keyup", () => {
  let search = queryResult.value.toLowerCase();
  queryList.innerHTML = "";
  let querysList = queryParse.filter(function (query) {
    return query.name.toLowerCase().includes(search?.toLowerCase());
  });
  parse(querysList);
});

const handleQuerypayload = () => {
  for (let i in queryPayload) {
    queryList.innerHTML += `<input type="text" name="send-${query}" value="${queryPayload[i]}" style="display: none" />`;
  }
};

function panelQueryToggle() {
  if (queryToggle == false) {
    queryToggle = true;
    $(`#${query}s-selector-container`).css("min-height", "315px");
    $(`#${query}s-search-container`).css("height", "235px");
    $(`#${query}s-search-container`).css("padding", "5px 0");
    $(`#${query}s-search-container`).css("border", "1px solid #938471");
    $(`.${query}-search-content`).css("height", "180px");
    $(`.${query}-arrow`).css("transform", "rotate(-90deg)");
    $(`.${query}s-search-btn`).css("display", "flex");
  } else {
    queryToggle = false;
    $(`#${query}s-selector-container`).css("min-height", "200px");
    $(`#${query}s-search-container`).css("height", "0px");
    $(`#${query}s-search-container`).css("padding", "0");
    $(`#${query}s-search-container`).css("border-top", "none");
    $(`#${query}s-search-container`).css("border-bottom", "none");
    $(`.${query}-search-content`).css("height", "0px");
    $(`.${query}-arrow`).css("transform", "rotate(90deg)");
    $(`.${query}s-search-btn`).css("display", "none");
  }
}

const handleQueryClick = (event) => {
  event.target.closest("div").children[0].click();
};

const handleQueryCheck = (event) => {
  if (event.target.checked) {
    queryCount += 1;
    queryPayload.push(event.target.value);
  } else {
    queryCount -= 1;
    for (let i in queryPayload) {
      if (queryPayload[i] == event.target.value) {
        queryPayload.splice(i, 1);
      }
    }
  }

  document.getElementById("selector-title").innerHTML =
    queryCount < 1
      ? `Ajouter un(e) nouvelle ${item}`
      : queryCount == 1
      ? `${queryCount} ${item} sélectionnée`
      : `${queryCount} ${item}s sélectionnées`;
};
