let items = document.getElementsByClassName('timeline-slot')

const setSelected = (event) => {
    values = Object.values(items).map((item) => {
        if (event.target.attributes.name?.value === item.attributes.name.value) {
            document.getElementsByName(item.attributes.name.value)[0].style.backgroundColor = "#008000";
        } else {
            document.getElementsByName(item.attributes.name.value)[0].style.backgroundColor = "#0076b8";
        }
    })
}