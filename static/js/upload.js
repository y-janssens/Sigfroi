let file = document.getElementById('id_avatar');
let upload = document.getElementById('avatar_url');
let avatar = document.getElementById('avatar_file_name').value;
let fake = document.getElementById('fake_id_avatar');

const handleUpload = (url) => {
    if (url.length) {
        fake.disabled = true;
        file.disabled = true;
    }
    handleCheck();
    avatar = url.split(/(\\|\/)/g).pop();
    console.log(avatar);
};

const handleCheck = () => {
    if (file.files.length) {
        avatar_url.disabled = true;
    }
};

const handleClear = (event) => {
    event.preventDefault();
    upload.value = null;
    avatar = '';
    file.value = null;
    fake.disabled = false;
    file.disabled = false;
    avatar_url.disabled = false;
};
