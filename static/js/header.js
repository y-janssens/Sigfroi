const svgs = [
    [
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512"><path d="M575.8 255.5C575.8 273.5 560.8 287.6 543.8 287.6H511.8L512.5 447.7C512.5 450.5 512.3 453.1 512 455.8V472C512 494.1 494.1 512 472 512H456C454.9 512 453.8 511.1 452.7 511.9C451.3 511.1 449.9 512 448.5 512H392C369.9 512 352 494.1 352 472V384C352 366.3 337.7 352 320 352H256C238.3 352 224 366.3 224 384V472C224 494.1 206.1 512 184 512H128.1C126.6 512 125.1 511.9 123.6 511.8C122.4 511.9 121.2 512 120 512H104C81.91 512 64 494.1 64 472V360C64 359.1 64.03 358.1 64.09 357.2V287.6H32.05C14.02 287.6 0 273.5 0 255.5C0 246.5 3.004 238.5 10.01 231.5L266.4 8.016C273.4 1.002 281.4 0 288.4 0C295.4 0 303.4 2.004 309.5 7.014L564.8 231.5C572.8 238.5 576.9 246.5 575.8 255.5L575.8 255.5z"/></svg>'
    ],

    [
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 512"><path d="M319.9 320c57.41 0 103.1-46.56 103.1-104c0-57.44-46.54-104-103.1-104c-57.41 0-103.1 46.56-103.1 104C215.9 273.4 262.5 320 319.9 320zM369.9 352H270.1C191.6 352 128 411.7 128 485.3C128 500.1 140.7 512 156.4 512h327.2C499.3 512 512 500.1 512 485.3C512 411.7 448.4 352 369.9 352zM512 160c44.18 0 80-35.82 80-80S556.2 0 512 0c-44.18 0-80 35.82-80 80S467.8 160 512 160zM183.9 216c0-5.449 .9824-10.63 1.609-15.91C174.6 194.1 162.6 192 149.9 192H88.08C39.44 192 0 233.8 0 285.3C0 295.6 7.887 304 17.62 304h199.5C196.7 280.2 183.9 249.7 183.9 216zM128 160c44.18 0 80-35.82 80-80S172.2 0 128 0C83.82 0 48 35.82 48 80S83.82 160 128 160zM551.9 192h-61.84c-12.8 0-24.88 3.037-35.86 8.24C454.8 205.5 455.8 210.6 455.8 216c0 33.71-12.78 64.21-33.16 88h199.7C632.1 304 640 295.6 640 285.3C640 233.8 600.6 192 551.9 192z"/></svg>'
    ],

    [
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 384 512"><path d="M256 0v128h128L256 0zM224 128L224 0H48C21.49 0 0 21.49 0 48v416C0 490.5 21.49 512 48 512h288c26.51 0 48-21.49 48-48V160h-127.1C238.3 160 224 145.7 224 128zM272 416h-160C103.2 416 96 408.8 96 400C96 391.2 103.2 384 112 384h160c8.836 0 16 7.162 16 16C288 408.8 280.8 416 272 416zM272 352h-160C103.2 352 96 344.8 96 336C96 327.2 103.2 320 112 320h160c8.836 0 16 7.162 16 16C288 344.8 280.8 352 272 352zM288 272C288 280.8 280.8 288 272 288h-160C103.2 288 96 280.8 96 272C96 263.2 103.2 256 112 256h160C280.8 256 288 263.2 288 272z"/></svg>'
    ],

    [
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 384 512"><path d="M112.1 454.3c0 6.297 1.816 12.44 5.284 17.69l17.14 25.69c5.25 7.875 17.17 14.28 26.64 14.28h61.67c9.438 0 21.36-6.401 26.61-14.28l17.08-25.68c2.938-4.438 5.348-12.37 5.348-17.7L272 415.1h-160L112.1 454.3zM191.4 .0132C89.44 .3257 16 82.97 16 175.1c0 44.38 16.44 84.84 43.56 115.8c16.53 18.84 42.34 58.23 52.22 91.45c.0313 .25 .0938 .5166 .125 .7823h160.2c.0313-.2656 .0938-.5166 .125-.7823c9.875-33.22 35.69-72.61 52.22-91.45C351.6 260.8 368 220.4 368 175.1C368 78.61 288.9-.2837 191.4 .0132zM192 96.01c-44.13 0-80 35.89-80 79.1C112 184.8 104.8 192 96 192S80 184.8 80 176c0-61.76 50.25-111.1 112-111.1c8.844 0 16 7.159 16 16S200.8 96.01 192 96.01z"/></svg>'
    ],

    [
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512"><path d="M544 64h-16V56C528 42.74 517.3 32 504 32S480 42.74 480 56V64H43.17C19.33 64 0 83.33 0 107.2v89.66C0 220.7 19.33 240 43.17 240c21.26 0 36.61 20.35 30.77 40.79l-40.69 158.4C27.41 459.6 42.76 480 64.02 480h103.8c14.29 0 26.84-9.469 30.77-23.21L226.4 352h94.58c24.16 0 45.5-15.41 53.13-38.28L398.6 240h36.1c8.486 0 16.62-3.369 22.63-9.373L480 208h64c17.67 0 32-14.33 32-32V96C576 78.33 561.7 64 544 64zM328.5 298.6C327.4 301.8 324.4 304 320.9 304H239.1L256 240h92.02L328.5 298.6zM480 160H64V128h416V160z"/></svg>'
    ],

    [
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><path d="M256-.0078C260.7-.0081 265.2 1.008 269.4 2.913L457.7 82.79C479.7 92.12 496.2 113.8 496 139.1C495.5 239.2 454.7 420.7 282.4 503.2C265.7 511.1 246.3 511.1 229.6 503.2C57.25 420.7 16.49 239.2 15.1 139.1C15.87 113.8 32.32 92.12 54.3 82.79L242.7 2.913C246.8 1.008 251.4-.0081 256-.0078V-.0078z"/></svg>'
    ],
    [
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512"><path d="M400 0H176c-26.5 0-48.1 21.8-47.1 48.2c.2 5.3 .4 10.6 .7 15.8H24C10.7 64 0 74.7 0 88c0 92.6 33.5 157 78.5 200.7c44.3 43.1 98.3 64.8 138.1 75.8c23.4 6.5 39.4 26 39.4 45.6c0 20.9-17 37.9-37.9 37.9H192c-17.7 0-32 14.3-32 32s14.3 32 32 32H384c17.7 0 32-14.3 32-32s-14.3-32-32-32H357.9C337 448 320 431 320 410.1c0-19.6 15.9-39.2 39.4-45.6c39.9-11 93.9-32.7 138.2-75.8C542.5 245 576 180.6 576 88c0-13.3-10.7-24-24-24H446.4c.3-5.2 .5-10.4 .7-15.8C448.1 21.8 426.5 0 400 0zM48.9 112h84.4c9.1 90.1 29.2 150.3 51.9 190.6c-24.9-11-50.8-26.5-73.2-48.3c-32-31.1-58-76-63-142.3zM464.1 254.3c-22.4 21.8-48.3 37.3-73.2 48.3c22.7-40.3 42.8-100.5 51.9-190.6h84.4c-5.1 66.3-31.1 111.2-63 142.3z"/></svg>'
    ],
    [
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 512"><path d="M0 488V171.3C0 145.2 15.93 121.6 40.23 111.9L308.1 4.753C315.7 1.702 324.3 1.702 331.9 4.753L599.8 111.9C624.1 121.6 640 145.2 640 171.3V488C640 501.3 629.3 512 616 512H568C554.7 512 544 501.3 544 488V223.1C544 206.3 529.7 191.1 512 191.1H128C110.3 191.1 96 206.3 96 223.1V488C96 501.3 85.25 512 72 512H24C10.75 512 0 501.3 0 488zM152 512C138.7 512 128 501.3 128 488V432H512V488C512 501.3 501.3 512 488 512H152zM128 336H512V400H128V336zM128 224H512V304H128V224z"/></svg>'
    ],

    [
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512"><path d="M463.1 474.7C465.1 486.7 460.2 498.9 450.2 506C440.3 513.1 427.2 514 416.5 508.3L288.1 439.8L159.8 508.3C149 514 135.9 513.1 126 506C116.1 498.9 111.1 486.7 113.2 474.7L137.8 328.1L33.58 225.9C24.97 217.3 21.91 204.7 25.69 193.1C29.46 181.6 39.43 173.2 51.42 171.5L195 150.3L259.4 17.97C264.7 6.954 275.9-.0391 288.1-.0391C300.4-.0391 311.6 6.954 316.9 17.97L381.2 150.3L524.9 171.5C536.8 173.2 546.8 181.6 550.6 193.1C554.4 204.7 551.3 217.3 542.7 225.9L438.5 328.1L463.1 474.7zM288 376.4L288.1 376.3L399.7 435.9L378.4 309.6L469.2 219.8L343.8 201.4L288.1 86.85L288 87.14V376.4z"/></svg>'
    ],

    [
        `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 384 512"><path d="M0 32C0 14.33 14.33 0 32 0H352C369.7 0 384 14.33 384 32C384 49.67 369.7 64 352 64V74.98C352 117.4 335.1 158.1 305.1 188.1L237.3 256L305.1 323.9C335.1 353.9 352 394.6 352 437V448C369.7 448 384 462.3 384 480C384 497.7 369.7 512 352 512H32C14.33 512 0 497.7 0 480C0 462.3 14.33 448 32 448V437C32 394.6 48.86 353.9 78.86 323.9L146.7 256L78.86 188.1C48.86 158.1 32 117.4 32 74.98V64C14.33 64 0 49.67 0 32zM96 64V74.98C96 100.4 106.1 124.9 124.1 142.9L192 210.7L259.9 142.9C277.9 124.9 288 100.4 288 74.98V64H96zM96 448H288V437C288 411.6 277.9 387.1 259.9 369.1L192 301.3L124.1 369.1C106.1 387.1 96 411.6 96 437V448z"/></svg>`
    ],
    [
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><path d="M96 96c0-35.3 28.7-64 64-64H448c35.3 0 64 28.7 64 64V416c0 35.3-28.7 64-64 64H80c-44.2 0-80-35.8-80-80V128c0-17.7 14.3-32 32-32s32 14.3 32 32V400c0 8.8 7.2 16 16 16s16-7.2 16-16V96zm64 24v80c0 13.3 10.7 24 24 24H424c13.3 0 24-10.7 24-24V120c0-13.3-10.7-24-24-24H184c-13.3 0-24 10.7-24 24zm0 184c0 8.8 7.2 16 16 16h96c8.8 0 16-7.2 16-16s-7.2-16-16-16H176c-8.8 0-16 7.2-16 16zm160 0c0 8.8 7.2 16 16 16h96c8.8 0 16-7.2 16-16s-7.2-16-16-16H336c-8.8 0-16 7.2-16 16zM160 400c0 8.8 7.2 16 16 16h96c8.8 0 16-7.2 16-16s-7.2-16-16-16H176c-8.8 0-16 7.2-16 16zm160 0c0 8.8 7.2 16 16 16h96c8.8 0 16-7.2 16-16s-7.2-16-16-16H336c-8.8 0-16 7.2-16 16z"/></svg>'
    ],
    [
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 384 512"><path d="M336 0h-288C22.38 0 0 22.38 0 48v416C0 489.6 22.38 512 48 512h288c25.62 0 48-22.38 48-48v-416C384 22.38 361.6 0 336 0zM64 208C64 199.2 71.2 192 80 192h32C120.8 192 128 199.2 128 208v32C128 248.8 120.8 256 112 256h-32C71.2 256 64 248.8 64 240V208zM64 304C64 295.2 71.2 288 80 288h32C120.8 288 128 295.2 128 304v32C128 344.8 120.8 352 112 352h-32C71.2 352 64 344.8 64 336V304zM224 432c0 8.801-7.199 16-16 16h-128C71.2 448 64 440.8 64 432v-32C64 391.2 71.2 384 80 384h128c8.801 0 16 7.199 16 16V432zM224 336c0 8.801-7.199 16-16 16h-32C167.2 352 160 344.8 160 336v-32C160 295.2 167.2 288 176 288h32C216.8 288 224 295.2 224 304V336zM224 240C224 248.8 216.8 256 208 256h-32C167.2 256 160 248.8 160 240v-32C160 199.2 167.2 192 176 192h32C216.8 192 224 199.2 224 208V240zM320 432c0 8.801-7.199 16-16 16h-32c-8.799 0-16-7.199-16-16v-32c0-8.801 7.201-16 16-16h32c8.801 0 16 7.199 16 16V432zM320 336c0 8.801-7.199 16-16 16h-32c-8.799 0-16-7.199-16-16v-32C256 295.2 263.2 288 272 288h32C312.8 288 320 295.2 320 304V336zM320 240C320 248.8 312.8 256 304 256h-32C263.2 256 256 248.8 256 240v-32C256 199.2 263.2 192 272 192h32C312.8 192 320 199.2 320 208V240zM320 144C320 152.8 312.8 160 304 160h-224C71.2 160 64 152.8 64 144v-64C64 71.2 71.2 64 80 64h224C312.8 64 320 71.2 320 80V144z"/></svg>'
    ],

    [
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512"><path d="M243.583 91.6027L323.695 138.384C326.575 140.026 326.68 144.583 323.695 146.225L228.503 201.854C225.623 203.55 222.22 203.444 219.549 201.854L124.357 146.225C121.425 144.636 121.373 139.973 124.357 138.384L204.417 91.6027V0L0 119.417V358.252L78.3843 312.477V218.914C78.3319 215.576 82.2066 213.192 85.0865 214.993L180.279 270.622C183.159 272.318 184.782 275.338 184.782 278.464V389.669C184.834 393.007 180.959 395.391 178.079 393.589L97.9673 346.808L19.583 392.583L224 512L428.417 392.583L350.033 346.808L269.921 393.589C267.093 395.338 263.114 393.06 263.218 389.669V278.464C263.218 275.126 265.051 272.159 267.721 270.622L362.914 214.993C365.741 213.245 369.72 215.47 369.616 218.914V312.477L448 358.252V119.417L243.583 0V91.6027Z"/></svg>'
    ],
    [
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><path fill="#938471" d="M125.7 160H176c17.7 0 32 14.3 32 32s-14.3 32-32 32H48c-17.7 0-32-14.3-32-32V64c0-17.7 14.3-32 32-32s32 14.3 32 32v51.2L97.6 97.6c87.5-87.5 229.3-87.5 316.8 0s87.5 229.3 0 316.8s-229.3 87.5-316.8 0c-12.5-12.5-12.5-32.8 0-45.3s32.8-12.5 45.3 0c62.5 62.5 163.8 62.5 226.3 0s62.5-163.8 0-226.3s-163.8-62.5-226.3 0L125.7 160z"/></svg>'
    ],
  
    [
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 512"><path d="M414.8 40.79L286.8 488.8C281.9 505.8 264.2 515.6 247.2 510.8C230.2 505.9 220.4 488.2 225.2 471.2L353.2 23.21C358.1 6.216 375.8-3.624 392.8 1.232C409.8 6.087 419.6 23.8 414.8 40.79H414.8zM518.6 121.4L630.6 233.4C643.1 245.9 643.1 266.1 630.6 278.6L518.6 390.6C506.1 403.1 485.9 403.1 473.4 390.6C460.9 378.1 460.9 357.9 473.4 345.4L562.7 256L473.4 166.6C460.9 154.1 460.9 133.9 473.4 121.4C485.9 108.9 506.1 108.9 518.6 121.4V121.4zM166.6 166.6L77.25 256L166.6 345.4C179.1 357.9 179.1 378.1 166.6 390.6C154.1 403.1 133.9 403.1 121.4 390.6L9.372 278.6C-3.124 266.1-3.124 245.9 9.372 233.4L121.4 121.4C133.9 108.9 154.1 108.9 166.6 121.4C179.1 133.9 179.1 154.1 166.6 166.6V166.6z"/></svg>'
    ],

    [
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512"><path d="M80 192V144C80 64.47 144.5 0 224 0C303.5 0 368 64.47 368 144V192H384C419.3 192 448 220.7 448 256V448C448 483.3 419.3 512 384 512H64C28.65 512 0 483.3 0 448V256C0 220.7 28.65 192 64 192H80zM144 192H304V144C304 99.82 268.2 64 224 64C179.8 64 144 99.82 144 144V192z"/></svg>'
    ]
];

const handleChange = () => {
    const buttons = document.getElementById('header-item-content').children;
    for (let i = 0; i < buttons.length; i++) {
        if (buttons[i].href === window.location.href) {
            buttons[i].classList.add('active-item');
        }
    }
};
window.onload = handleChange();

const handleSvgs = () => {
    const classes = document.getElementsByClassName('item-svg');
    for (let i = 0; i < classes.length; i++) {
        classes[i].innerHTML = svgs[i];
    }
};

window.onload = handleSvgs();
