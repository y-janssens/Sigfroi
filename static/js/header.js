const handleChange = () => {
  const buttons = document.getElementById("header-item-content").children;
  for (let i = 0; i < buttons.length; i++) {
    if (buttons[i].href === window.location.href) {
      buttons[i].classList.add("active-item");
    }
  }
};
window.onload = handleChange();
