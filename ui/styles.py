APP_STYLE = """

QMainWindow {
    background-color: #202124;
}


/* =========================
   CONTENEDOR PRINCIPAL
   ========================= */

QWidget#centralContainer {
    background-color: #202124;
}



/* =========================
   SIDEBAR
   ========================= */

QFrame#sidebar {
    background-color: #292a2d;

    border-right: 1px solid #3f4145;
}


/* =========================
   BARRA SUPERIOR
   ========================= */

QFrame#topbar {
    background-color: #292a2d;

    border-bottom: 1px solid #3f4145;
}


/* =========================
   TÍTULO DE LA PANTALLA
   ========================= */

QWidget#header {
    background-color: white;
    border: none;
}


QLabel#screenTitle {
    color: #202124;

    background-color: transparent;

    font-family: Arial;

    font-size: 15px;

    font-weight: normal;

    padding: 0px;
}


/* =========================
   TÍTULO DEL SIDEBAR
   ========================= */

QLabel#sidebarTitle {
    color: white;

    font-family: Arial;

    font-size: 15px;

    font-weight: normal;
}


/* ==========
    BOTONES
   ========== */

QPushButton {
    color: #d4d4d4;

    background-color: transparent;

    border: none;

    border-radius: 5px;

    text-align: left;

    padding-left: 18px;

    font-family: Arial;

    font-size: 14px;
}


QPushButton:hover {
    background-color: #35363a;

    color: white;
}


QPushButton:pressed {
    background-color: #45464a;
}

QPushButton#switchLeft,
QPushButton#switchRight {
    background-color: #eeeeee;
    color: #333333;

    border: 1px solid #bdbdbd;

    padding: 8px 25px;

    font-family: Arial;
    font-size: 14px;
}


QPushButton#switchLeft {
    border-top-left-radius: 8px;
    border-bottom-left-radius: 8px;
}


QPushButton#switchRight {
    border-top-right-radius: 8px;
    border-bottom-right-radius: 8px;
}


QPushButton#switchLeft:checked,
QPushButton#switchRight:checked {
    background-color: #3c4043;
    color: white;
}


QFrame#dataPanel {
    background-color: white;

    border: 1px solid #dcdcdc;

    border-radius: 8px;
}

/* =========================
   PÁGINAS
   ========================= */

QStackedWidget#pages {
    background-color: white;
    border: none;
}

"""