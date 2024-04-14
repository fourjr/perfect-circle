function solve() {
    const allDiv = document.getElementsByTagName('div');
    let drawContainer = null;
    let clientRect = null;
    for (d of allDiv) {
        if (d.className === "" && d.id === "" && d.getBoundingClientRect().width !== 0) {
            drawContainer = d;
            clientRect = d.getBoundingClientRect();
            break;
        }
    }

    const circleRadius = clientRect.width / 2 * 0.8;

    const center = {
        x: clientRect.width / 2 + clientRect.left,
        y: clientRect.height / 2 + clientRect.top
    }

    const x = t => circleRadius * Math.cos(t) + center.x
    const y = t => circleRadius * Math.sin(t) + center.y

    // start drawing circle
    const mdEvent = new Event("mousedown");
    mdEvent.pageX = x(0);
    mdEvent.pageY = y(0);
    drawContainer.dispatchEvent(mdEvent);

    for (i = 0; i < 360; i++) {
        const mmEvent = new Event("mousemove");
        mmEvent.pageX = x(i * Math.PI / 180);
        mmEvent.pageY = y(i * Math.PI / 180);
        drawContainer.dispatchEvent(mmEvent);
    }

    drawContainer.dispatchEvent(new Event("mouseup"));
}