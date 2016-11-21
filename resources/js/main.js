$(function () {
    /* Dotdotdot plugin configuration*/

    $(".post-preview").dotdotdot({
        ellipsis: '... ',
        wrap: 'word',
        fallbackToLetter: true,
        after: "a.readmore",
        watch: true,
        height: null,
        tolerance: 0,
        lastCharacter: {
            remove: [' ', ',', ';', '.', '!', '?'],
            noEllipsis: []
        }
    });
});