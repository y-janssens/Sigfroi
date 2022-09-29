const handleBackup = (value, name) => {
    const file = document.createElement('a');
    file.href = window.URL.createObjectURL(new Blob([value], { type: 'application/json' }));
    file.download = `${name}.json`;
    file.click();
};
