/* Scripts for FullCalendar */

document.addEventListener("DOMContentLoaded", function () {
    const calendarEl = document.getElementById("calendar");
    const selectedDateEl = document.getElementById("selected-date");
    const bookingDateInput = document.getElementById("booking_date");
    const guestInput = document.getElementById("guests");
    const bookingTimeInput = document.getElementById("booking_time");

    if (!calendarEl || !bookingDateInput || !guestInput || !bookingTimeInput) {
        return;
    }

    async function loadAvailableTimes() {
        const selectedDate = bookingDateInput.value;
        const guests = guestInput.value;

        bookingTimeInput.replaceChildren();

        if (!selectedDate) {
            bookingTimeInput.add(
                new Option("Select a date", "")
            );
            bookingTimeInput.disabled = true;
            return;
        }

        bookingTimeInput.add(
            new Option("Checking availability...", "")
        );
        bookingTimeInput.disabled = true;

        try {
            const url = new URL(
                "/book/availability/",
                window.location.origin
            );

            url.searchParams.set("date", selectedDate);
            url.searchParams.set("guests", guests);

            const response = await fetch(url);

            if (!response.ok) {
                throw new Error("Could not load availability.");
            }
            const data = await response.json();

            bookingTimeInput.replaceChildren();

            if (data.times.length === 0) {
                bookingTimeInput.add(
                    new Option("No times available", "")
                );
                return;
            }

            bookingTimeInput.add(
                new Option("Choose a time", "")
            );

            data.times.forEach(function (slot) {
                bookingTimeInput.add(
                    new Option(slot.label, slot.value)
                );
            });

            bookingTimeInput.disabled = false;

        } catch (error) {
            console.error("Availability error:", error);

            bookingTimeInput.replaceChildren(
                new Option("Unable to load times. Try again.", "")
            );
        }
    }

    const calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: "dayGridMonth",
        height: "auto",

        validRange: {
            start: new Date().toISOString().slice(0, 10)
        },

        dateClick: function (info) {
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
            bookingDateInput.value = info.dateStr;

            selectedDateEl.textContent = "Selected date: " + info.dateStr;

            loadAvailableTimes();
        }
    });

    calendar.render();

    bookingDateInput.addEventListener(
        "change",
        function () {
            // Clear the old highlight when the input changes.
            calendarEl.querySelectorAll(
                ".selected-date-cell"
            ).forEach(function (cell) {
                cell.classList.remove("selected-date-cell");
            });

            selectedDateEl.textContent =
                bookingDateInput.value
                    ? "Selected date: " + bookingDateInput.value
                    : "Please select a date.";

            loadAvailableTimes();
        }
    );
    guestsInput.addEventListener(
        "change",
        loadAvailableTimes
    );
});