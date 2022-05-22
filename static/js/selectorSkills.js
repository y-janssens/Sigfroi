let skillToggle = false;
let skillCount = 0;

axios.get(`${window.location.origin}/api/competences/`).then(function (response) {
  skills = response.data;
  document.getElementById("skills-list").innerHTML = "";
  for (let i = 0; i < skills.length; i++) {
    document.getElementById(
      "skills-list"
    ).innerHTML += `<div class="skill-search-content-item"><input type="checkbox" onchange="handleSkillCheck(event)" value="${skills[i].name}" name="skill-request" /><label for="${skills[i].name}" class="skill-search-content-item-label" onclick="handleSkillClick(event)">${skills[i].name}</label></div>`;
  }
});

function panelSkillToggle() {
  if (skillToggle == false) {
    skillToggle = true;
    $("#skills-selector-container").css("min-height", "315px");
    $("#skills-search-container").css("height", "235px");
    $("#skills-search-container").css("padding", "5px 0");
    $("#skills-search-container").css("border", "1px solid #938471");
    $(".skill-search-content").css("height", "180px");
    $(".skill-arrow").css("transform", "rotate(-90deg)");
    $(".skills-search-btn").css("display", "flex");
  } else {
    skillToggle = false;
    $("#skills-selector-container").css("min-height", "200px");
    $("#skills-search-container").css("height", "0px");
    $("#skills-search-container").css("padding", "0");
    $("#skills-search-container").css("border-top", "none");
    $("#skills-search-container").css("border-bottom", "none");
    $(".skill-search-content").css("height", "0px");
    $(".skill-arrow").css("transform", "rotate(90deg)");
    $(".skills-search-btn").css("display", "none");
  }
}

const handleSkillClick = (event) => {
  event.target.closest("div").children[0].click();
};

const handleSkillCheck = (event) => {
  if (event.target.checked) {
    skillCount += 1;
  } else {
    skillCount -= 1;
  }

  document.getElementById("selector-title").innerHTML =
    skillCount < 1
      ? "Ajouter une nouvelle compétence"
      : skillCount == 1
      ? `${skillCount} compétence sélectionnée`
      : `${skillCount} compétences sélectionnées`;
};

let skillResult = document.getElementById("skill_search_bar_input");
skillResult.addEventListener("keyup", () => {
  let query = skillResult.value;
  document.getElementById("skills-list").innerHTML = "";
  let skillsList = skills.filter(function (skill) {
    return skill.name.toLowerCase().includes(query?.toLowerCase());
  });

  skillsList.map((skill) => {
    return (document.getElementById(
      "skills-list"
    ).innerHTML += `<div class="skill-search-content-item"><input type="checkbox" onchange="handleSkillCheck(event)" value="${skill.name}" name="skill-request" /><label for="${skill.name}" class="skill-search-content-item-label" onclick="handleSkillClick(event)">${skill.name}</label></div>`);
  });
});
