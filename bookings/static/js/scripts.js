/* Scripts for FullCalendar */

document.addEventListener("DOMContentLoaded", function () {
    const calendarEl = document.getElementById("calendar");
    const selectedDateEl = document.getElementById("selected-date");
    const bookingDateInput = document.getElementById("booking_date");

    const calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: "dayGridMonth",
        height: "auto",

        dateClick: function (info) {
            // Removes the previous selection.
            calendarEl.querySelectorAll(".selected-date-cell").forEach(
                function (cell) {
                    cell.classList.remove("selected-date-cell");
                }
            );

            // Highlights the newly selected date cell.
            info.dayEl.classList.add("selected-date-cell");

            // Stores and displays the selected date.
            bookingDateInput.value = info.dateStr;
            selectedDateEl.textContent =
                "Selected date: " + info.dateStr;
        }
    });

    calendar.render();
});