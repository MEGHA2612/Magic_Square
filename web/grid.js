// --------------------------------
// GAME SETTINGS
// --------------------------------
const GRID_SIZE = 3;

// --------------------------------
// STREAMLIT COMPONENT
// --------------------------------
export default function ({
    parentElement,
    data,
    setTriggerValue
}) {

    // --------------------------------
    // GET ELEMENTS
    // --------------------------------

    const timerElement = parentElement.querySelector("#timer");

    const board = parentElement.querySelector("#game-board");

    const checkButton = parentElement.querySelector("#check-button");

    const clearButton = parentElement.querySelector("#clear-button");

    const hintButton = parentElement.querySelector("#hint-button");

    // --------------------------------
    // INITIALIZE COMPONENT STATE
    // --------------------------------
    if (!parentElement._gameState) {
        parentElement._gameState = {
            seconds: 0,
            running: true,
            interval: null,
            restartHandled: false,
            hintListenerAdded: false,
            checkListenerAdded: false,
            clearListenerAdded: false
        };
    }

    const gameState = parentElement._gameState;

    // --------------------------------
    // UPDATE TIMER
    // --------------------------------
    function updateTimer() {
        if (!gameState.running) {
            return;
        }

        gameState.seconds++;

        const minutes = Math.floor(gameState.seconds / 60);

        const seconds = gameState.seconds % 60;

        const minutesText = String(minutes).padStart(2,"0");

        const secondsText = String(seconds).padStart(2,"0");

        timerElement.innerText = "⏱️ " + minutesText + ":" + secondsText;
    }

    // --------------------------------
    // START TIMER
    // --------------------------------
    if (gameState.interval === null) {
        gameState.interval = setInterval(updateTimer, 1000);
    }

    // --------------------------------
    // CREATE GAME GRID
    // --------------------------------
    if (board.querySelectorAll(".game-cell").length === 0) {
        for (let row = 0; row < GRID_SIZE; row++) {
            for (let col = 0; col < GRID_SIZE; col++) {
                const cell = document.createElement("div")
                cell.className = "game-cell";
                cell.contentEditable = "true";
                cell.dataset.row = row;
                cell.dataset.col = col;

                // --------------------------------
                // CELL CLICK
                // --------------------------------
                cell.addEventListener(
                    "click",
                    function () {
                        parentElement
                            .querySelectorAll(
                                ".game-cell"
                            )
                            .forEach(
                                function (item) {
                                    item.classList
                                        .remove(
                                            "selected"
                                        );
                                }
                            );

                        cell.classList.add("selected");
                        cell.focus();
                    }
                );

                // --------------------------------
                // KEYBOARD INPUT
                // --------------------------------
                cell.addEventListener(
                    "keydown",
                    function (event) {

                        // ------------------------
                        // ENTER
                        // ------------------------
                        if (event.key === "Enter") {
                            event.preventDefault();
                            cell.innerText =cell.innerText.trim();
                            return;
                        }

                        // ------------------------
                        // BACKSPACE
                        // ------------------------
                        if (event.key === "Backspace") {
                            event.preventDefault();
                            if (cell.contentEditable === "false") {
                                return;
                            }
                            cell.innerText = "";
                            cell.classList.remove("player-number");
                            return;
                        }

                        // ------------------------
                        // DELETE
                        // ------------------------
                        if (event.key === "Delete") {
                            event.preventDefault();
                            if (cell.contentEditable === "false") {
                                return;
                            }

                            cell.innerText = "";
                            cell.classList.remove("player-number");
                            return;
                        }

                        // ------------------------
                        // ONLY 1–9
                        // ------------------------
                        if (!/^[1-9]$/.test(event.key)) {
                            event.preventDefault();
                            return;
                        }

                        // ------------------------
                        // HINT CELLS CANNOT EDIT
                        // ------------------------
                        if (cell.contentEditable === "false") {
                            event.preventDefault();
                            return;
                        }

                        // ------------------------
                        // INSERT PLAYER NUMBER
                        // ------------------------
                        event.preventDefault();
                        cell.innerText = event.key;
                        cell.classList.add("player-number");
                    }
                );

                board.appendChild(cell);
            }
        }
    }

    // --------------------------------
    // GET CURRENT GRID
    // --------------------------------
    function getGrid() {
        const grid = [];
        const cells = parentElement.querySelectorAll(".game-cell");

        for (let row = 0; row < GRID_SIZE; row++) {
            const currentRow = [];
            for (let col = 0; col < GRID_SIZE; col++) {
                const index = row * GRID_SIZE + col;
                const value = cells[index].innerText.trim();
                if (value === "") {
                    currentRow.push(0);
                }
                else {
                    currentRow.push(parseInt(value));
                }
            }
            grid.push(currentRow);
        }
        return grid;
    }

    // --------------------------------
    // HANDLE RESTART
    // --------------------------------
    if (data?.restart === true && !gameState.restartHandled) {
        gameState.restartHandled = true;

        // ------------------------
        // CLEAR GRID
        // ------------------------
        parentElement
            .querySelectorAll(
                ".game-cell"
            )
            .forEach(
                function (cell) {
                    cell.innerText = "";
                    cell.classList.remove("selected");
                    cell.classList.remove("player-number");
                    cell.classList.remove("hint-number");
                    cell.contentEditable = "true";
                }
            );

        // ------------------------
        // RESET TIMER
        // ------------------------
        gameState.seconds = 0;
        gameState.running = true;
        timerElement.innerText = "⏱️ 00:00";
    }

    // --------------------------------
    // ALLOW FUTURE RESTART
    // --------------------------------
    if (data?.restart !== true) {
        gameState.restartHandled = false;
    }

    // --------------------------------
    // CHECK BUTTON
    // --------------------------------
    if (!gameState.checkListenerAdded) {
        gameState.checkListenerAdded = true;
        checkButton.addEventListener(
            "click",
            function () {
                // ------------------------
                // STOP TIMER
                // ------------------------
                gameState.running = false;

                // ------------------------
                // GET GRID
                // ------------------------
                const grid = getGrid();

                // ------------------------
                // GET ELAPSED TIME
                // ------------------------
                const elapsedSeconds = gameState.seconds;

                // ------------------------
                // SEND TO PYTHON
                // ------------------------
                setTriggerValue(
                    "check",
                    {
                        grid: grid,
                        elapsed: elapsedSeconds
                    }
                );
            }
        );
    }

    // --------------------------------
    // CLEAR BUTTON
    // --------------------------------
    if (!gameState.clearListenerAdded) {
        gameState.clearListenerAdded = true;
        clearButton.addEventListener(
            "click",
            function () {
                parentElement
                    .querySelectorAll(
                        ".game-cell"
                    )
                    .forEach(
                        function (cell) {
                            // Don't remove
                            // hint cells
                            if (cell.classList.contains("hint-number")) {
                                return;
                            }
                            cell.innerText = "";
                            cell.classList.remove("selected");
                            cell.classList.remove("player-number");
                        }
                    );
            }
        );
    }

    // --------------------------------
    // HINT BUTTON
    // --------------------------------
    if (!gameState.hintListenerAdded) {
        gameState.hintListenerAdded = true;
        hintButton.addEventListener(
            "click",
            function () {
                // ------------------------
                // GET HINT COUNT
                // ------------------------
                const hintsLeft = data?.hints_left ?? 0;

                // ------------------------
                // NO HINTS LEFT
                // ------------------------
                if (hintsLeft <= 0) {
                    return;
                }

                // ------------------------
                // GET CURRENT GRID
                // ------------------------
                const grid = getGrid();

                // ------------------------
                // ASK PYTHON FOR HINT
                // ------------------------
                setTriggerValue("hint", {grid: grid});
            }
        );
    }

    // --------------------------------
    // HINT BUTTON STATE
    // --------------------------------
    const hintsLeft =data?.hints_left ?? 0;

    hintButton.disabled = hintsLeft <= 0;

    // --------------------------------
    // APPLY RETURNED HINT
    // --------------------------------
    if (data?.hint_result) {
        const hintResult = data.hint_result;
        const cells = parentElement.querySelectorAll(".game-cell");
        const index = hintResult.row * GRID_SIZE + hintResult.col;
        const cell = cells[index];

        if (cell && cell.innerText.trim() === "") {
            cell.innerText = hintResult.value;
            cell.classList.add("hint-number");
            cell.contentEditable = "false";
        }
    }
}