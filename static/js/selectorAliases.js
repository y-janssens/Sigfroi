let aliaseToggle = false;
let aliasesCount = 0;
let aliasePayload = []
let aliaseList = document.getElementById("aliases-list");

axios.get(`${window.location.origin}/api/fiches/`).then(function (response) {
  aliases = response.data;
  aliaseList.innerHTML = "";
  for (let i in aliases) {
    aliaseList.innerHTML += `<div class="alias-search-content-item"><input type="checkbox" onchange="handleAliasCheck(event)" value="${aliases[i].name}" name="alias-request" /><label for="${aliases[i].name}" class="alias-search-content-item-label" onclick="handleAliasClick(event)">${aliases[i].name}</label></div>`;
  }
});

const handleAliasPayload = () => {
  for (let i in aliasePayload) {
    aliaseList.innerHTML += `<input type="text" name="send-aliases" value="${aliasePayload[i]}" style="display: none" />`
  }
};

function panelaliaseToggle() {

  if (aliaseToggle == false) {
    aliaseToggle = true;
    $("#aliases-selector-container").css("min-height", "315px");
    $("#aliases-search-container").css("height", "235px");
    $("#aliases-search-container").css("padding", "5px 0");
    $("#aliases-search-container").css("border", "1px solid #938471");
    $(".alias-search-content").css("height", "180px");
    $(".alias-arrow").css("transform", "rotate(-90deg)");
    $(".aliases-search-btn").css("display", "flex");
  } else {
    aliaseToggle = false;
    $("#aliases-selector-container").css("min-height", "200px");
    $("#aliases-search-container").css("height", "0px");
    $("#aliases-search-container").css("padding", "0");
    $("#aliases-search-container").css("border-top", "none");
    $("#aliases-search-container").css("border-bottom", "none");
    $(".alias-search-content").css("height", "0px");
    $(".alias-arrow").css("transform", "rotate(90deg)");
    $(".aliases-search-btn").css("display", "none");
  }
}

const handleAliasClick = (event) => {
  event.target.closest("div").children[0].click();
};

const handleAliasCheck = (event) => {
  if (event.target.checked) {
    aliasesCount += 1;
    aliasePayload.push(event.target.value)
  } else {
    aliasesCount -= 1;
    for (let i in aliasePayload) {
      if (aliasePayload[i] == event.target.value) {
        aliasePayload.splice(i, 1);
      }
    }
  }

  document.getElementById("alias-selector-title").innerHTML =
    aliasesCount < 1
      ? "Ajouter un nouvel alias"
      : aliasesCount == 1
      ? `${aliasesCount} alias sélectionné`
      : `${aliasesCount} alias sélectionnés`;
};

let aliaseResult = document.getElementById("alias_search_bar_input");
aliaseResult.addEventListener("keyup", () => {
  let query = aliaseResult.value;
  aliaseList.innerHTML = "";
  let aliasesList = aliases.filter(function (aliase) {
    return aliase.name.toLowerCase().includes(query?.toLowerCase());
  });

  aliasesList.map((aliase) => {
    return (aliaseList.innerHTML += `<div class="alias-search-content-item"><input type="checkbox" onchange="handleAliasCheck(event)" value="${aliase.name}" name="alias-request" /><label for="${aliase.name}" class="alias-search-content-item-label" onclick="handleAliasClick(event)">${aliase.name}</label></div>`);
  });
});
