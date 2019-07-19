document.addEventListener("DOMContentLoaded", function(event) {
    var app = document.getElementById('typewriter');

    var typewriter = new Typewriter(app, {
        loop: false
    });

    typewriter.typeString('Let\'s Hack')
        .pauseFor(2500)
        .deleteChars(4)
        .typeString("Make")
        .pauseFor(2500)
        .deleteChars(4)
        .typeString("Innovate")
        .pauseFor(2500)
        .start();
});