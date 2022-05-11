let toggle = false;
let count = 0;

axios.get(`${window.location.origin}/api/competences/`).then(function (response) {
  skills = response.data;
  document.getElementById("skills-list").innerHTML = "";
  for (let i = 0; i < skills.length; i++) {
    document.getElementById(
      "skills-list"
    ).innerHTML += `<div class="skill-search-content-item"><input type="checkbox" onchange="handleCheck(event)" value="${skills[i].name}" name="skill-request" /><label for="${skills[i].name}" class="skill-search-content-item-label" onclick="handleClick(event)">${skills[i].name}</label></div>`;
  }
});

function panelToggle() {
  if (toggle == false) {
    toggle = true;
    $("#skills-selector-container").css("min-height", "315px");
    $("#skills-search-container").css("height", "235px");
    $("#skills-search-container").css("padding", "5px 0");
    $("#skills-search-container").css("border", "1px solid #938471");
    $(".skill-search-content").css("height", "180px");
    $(".arrow").css("transform", "rotate(-90deg)");
    $(".skills-search-btn").css("display", "flex");
  } else {
    toggle = false;
    $("#skills-selector-container").css("min-height", "200px");
    $("#skills-search-container").css("height", "0px");
    $("#skills-search-container").css("padding", "0");
    $("#skills-search-container").css("border-top", "none");
    $("#skills-search-container").css("border-bottom", "none");
    $(".skill-search-content").css("height", "0px");
    $(".arrow").css("transform", "rotate(90deg)");
    $(".skills-search-btn").css("display", "none");
  }
}

const handleClick = (event) => {
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

let result = document.getElementById("skill_search_bar_input");
result.addEventListener("keyup", () => {
  let query = result.value;
  document.getElementById("skills-list").innerHTML = "";
  let skillsList = skills.filter(function (skill) {
    return skill.name.toLowerCase().includes(query?.toLowerCase());
  });

  skillsList.map((skill) => {
    return (document.getElementById(
      "skills-list"
    ).innerHTML += `<div class="skill-search-content-item"><input type="checkbox" onchange="handleCheck(event)" value="${skill.name}" name="skill-request" /><label for="${skill.name}" class="skill-search-content-item-label" onclick="handleClick(event)">${skill.name}</label></div>`);
  });
});
