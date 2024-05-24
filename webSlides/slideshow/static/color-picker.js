window.addEventListener("load", () =>{
    const colorItems = document.querySelectorAll('.color-item');
    const colorFonts = document.querySelectorAll('.color-font');
    const colorInput = document.getElementById('selected-color');
    const colorFontInput = document.getElementById('selected-font');

    
    const currentColor = colorInput.value;
    const currentfontColor = colorFontInput.value;

    if (currentColor && currentfontColor) {
        document.getElementById(currentColor).style.outline = 'auto';
        document.getElementById(currentColor).style.transform = 'scale(1.5)';
        document.getElementById(currentfontColor).style.outline = 'auto';
        document.getElementById(currentfontColor).style.transform = 'scale(1.5)';
    }

    colorItems.forEach(item => {
        item.addEventListener('click', function(){
            const idSelected = this.id;
            colorInput.value = idSelected;
            colorItems.forEach(el => el.style.outline = 'none');
            colorItems.forEach(el => el.style.transform = 'scale(1)');

            this.style.outline = 'auto';
            this.style.transform = 'scale(1.5)';
        })
    })

    colorFonts.forEach(item => {
        item.addEventListener('click', function(){
            const idSelected = this.id;
            colorFontInput.value = idSelected;
            colorFonts.forEach(el => el.style.outline = 'none');
            colorFonts.forEach(el => el.style.transform = 'scale(1)');

            this.style.outline = 'auto';
            this.style.transform = 'scale(1.5)';
        })
    })
})
