/* let toggle = false;
let count = 0;

axios.get(`${window.location.origin}/api/competences/`).then(function (response) {
  stuffs = response.data;
  document.getElementById("stuffs-list").innerHTML = "";
  for (let i = 0; i < stuffs.length; i++) {
    document.getElementById(
      "stuffs-list"
    ).innerHTML += `<div class="stuff-search-content-item"><input type="checkbox" onchange="handleCheck(event)" value="${stuffs[i].name}" name="stuff-request" /><label for="${stuffs[i].name}" class="stuff-search-content-item-label" onclick="handleClick(event)">${stuffs[i].name}</label></div>`;
  }
}); */

function panelStuffToggle() {
  if (toggle == false) {
    toggle = true;
    $("#stuffs-selector-container").css("min-height", "315px");
    $("#stuffs-search-container").css("height", "235px");
    $("#stuffs-search-container").css("padding", "5px 0");
    $("#stuffs-search-container").css("border", "1px solid #938471");
    $(".stuff-search-content").css("height", "180px");
    $(".arrow").css("transform", "rotate(-90deg)");
    $(".stuffs-search-btn").css("display", "flex");
  } else {
    toggle = false;
    $("#stuffs-selector-container").css("min-height", "200px");
    $("#stuffs-search-container").css("height", "0px");
    $("#stuffs-search-container").css("padding", "0");
    $("#stuffs-search-container").css("border-top", "none");
    $("#stuffs-search-container").css("border-bottom", "none");
    $(".stuff-search-content").css("height", "0px");
    $(".arrow").css("transform", "rotate(90deg)");
    $(".stuffs-search-btn").css("display", "none");
  }
}

/* const handleClick = (event) => {
  event.target.closest("div").children[0].click();
};

const handleCheck = (event) => {
  if (event.target.checked) {
    count += 1;
  } else {
    count -= 1;
  }

  document.getElementById("selector-title").innerHTML =
    count < 1
      ? "Ajouter une nouvelle compétence"
      : count == 1
      ? `${count} compétence sélectionnée`
      : `${count} compétences sélectionnées`;
};

let result = document.getElementById("stuff_search_bar_input");
result.addEventListener("keyup", () => {
  let query = result.value;
  document.getElementById("stuffs-list").innerHTML = "";
  let stuffsList = stuffs.filter(function (stuff) {
    return stuff.name.toLowerCase().includes(query?.toLowerCase());
  });

  stuffsList.map((stuff) => {
    return (document.getElementById(
      "stuffs-list"
    ).innerHTML += `<div class="stuff-search-content-item"><input type="checkbox" onchange="handleCheck(event)" value="${stuff.name}" name="stuff-request" /><label for="${stuff.name}" class="stuff-search-content-item-label" onclick="handleClick(event)">${stuff.name}</label></div>`);
  });
}); */
