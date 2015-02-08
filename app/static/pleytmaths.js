/**
 * Created by liam on 2/8/15.
 */
function show_image(src, width, height, alt) {
    var img = document.createElement("img");
    img.class='pleyt';
    img.src = src;
    img.width = width;
    img.height = height;
    img.alt = alt;

    // This next line will just add it to the <body> tag
    document.body.appendChild(img);
}

function playtmaths(score){
    var names = ['static/img/pleyt1.png',
             'static/img/pleyt2.png',
             'static/img/pleyt3.png',
             'static/img/pleyt4.png',
             'static/img/pleyt5.png',
             'static/img/pleyt6.png',
             'static/img/pleyt7.png',
             'static/img/pleyt8.png',
             'static/img/pleyt9.png',
             'static/img/pleyt10.png']
    var score = score.toFixed(1)*10;
    var numfull = score/10;
    var numsmall = score%10;

    for (var ii=0; ii<numfull; ii++)
        show_image(names[09],160,160,'plates, bitch')

    if (numsmall > 0)
        show_image(names[numsmall-1],160,160,'littleplates,bitch')

}
