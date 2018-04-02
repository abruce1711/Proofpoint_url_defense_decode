function copy_text(){
    var text =  document.getElementById("field");
    text.select();
    document.execCommand("Copy");
    document.getSelection().removeAllRanges();
    document.activeElement.blur();
    document.getElementById("field").style.backgroundColor = "rgba(71, 132, 255, 0.5)";

    setTimeout(function(){
        document.getElementById("field").style.backgroundColor = "white"
    }, 800);
}