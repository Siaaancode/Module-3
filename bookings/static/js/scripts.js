/* Scripts for FullCalendar */

document.addEventListener("DOMContentLoaded", function () {
    const calendarEl = document.getElementById("calendar");
    const selectedDateEl = document.getElementById("selected-date");
    const bookingDateInput = document.getElementById("booking_date");

    const calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: "dayGridMonth",
        height: "auto",

        dateClick: function (info) {
            bookingDateInput.value = info.dateStr;

            selectedDateEl.textContent =
                "Selected date: " + info.dateStr;
        }
    });

    calendar.render();
});