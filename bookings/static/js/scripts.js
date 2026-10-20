/* Scripts for FullCalendar */

document.addEventListener("DOMContentLoaded", function () {
    const calendarEl = document.getElementById("calendar");
    const selectedDateEl = document.getElementById("selected-date");
    const bookingDateInput = document.getElementById("booking_date");
    const guestInput = document.getElementById("guests");
    const bookingTimeInput = document.getElementById("booking_time");

    // Stop the script if the required booking form elements are missing.
    if (!calendarEl || !bookingDateInput || !guestInput || !bookingTimeInput) {
        return;
    }

    // Fetch available booking times for the selected date and party size.
    async function loadAvailableTimes() {
        const selectedDate = bookingDateInput.value;
        const guests = guestInput.value;

        // Clear any previously displayed booking times.
        bookingTimeInput.replaceChildren();

        // Ask the customer to select a date before loading times.
        if (!selectedDate) {
            bookingTimeInput.add(
                new Option("Select a date", "")
            );
            bookingTimeInput.disabled = true;
            return;
        }

        // Disable the dropdown while availability is being checked.
        bookingTimeInput.add(
            new Option("Checking availability...", "")
        );
        bookingTimeInput.disabled = true;

        try {
            // Build the URL for the Django availability endpoint.
            const url = new URL(
                "/book/availability/",
                window.location.origin
            );

            // Pass the selected date and number of guests to Django.
            url.searchParams.set("date", selectedDate);
            url.searchParams.set("guests", guests);

            // Request the available booking times from the server.
            const response = await fetch(url);

            // Handle unsuccessful HTTP responses.
            if (!response.ok) {
                throw new Error("Could not load availability.");
            }

            // Convert the server's JSON response into a JavaScript object.
            const data = await response.json();

            // Remove the loading message before displaying the results.
            bookingTimeInput.replaceChildren();

            // Inform the customer if no booking times are available.
            if (data.times.length === 0) {
                bookingTimeInput.add(
                    new Option("No times available", "")
                );
                return;
            }

            // Add a placeholder prompting the customer to choose a time.
            bookingTimeInput.add(
                new Option("Choose a time", "")
            );

            // Add each available time to the dropdown.
            data.times.forEach(function (slot) {
                bookingTimeInput.add(
                    new Option(slot.label, slot.value)
                );
            });

            // Enable the dropdown so the customer can select a time.
            bookingTimeInput.disabled = false;

        } catch (error) {
            // Log the error for debugging if availability cannot be loaded.
            console.error("Availability error:", error);

            // Display an error message in the booking time dropdown.
            bookingTimeInput.replaceChildren(
                new Option("Unable to load times. Try again.", "")
            );
        }
    }

    // Create the FullCalendar month view inside the calendar element.
    const calendar = new FullCalendar.Calendar(calendarEl, {
        // Display the calendar by month when it first loads.
        initialView: "dayGridMonth",
        height: "auto",

        // Prevent customers from selecting dates in the past.
        validRange: {
            start: new Date().toISOString().slice(0, 10)
        },

        // Handle a customer clicking on a calendar date.
        dateClick: function (info) {
            // Remove the highlight from any previously selected date.
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

            // Load available booking times for the selected date.
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

            // Display the selected date or prompt the customer to choose one.
            selectedDateEl.textContent =
                bookingDateInput.value
                    ? "Selected date: " + bookingDateInput.value
                    : "Please select a date.";

            // Refresh available times for the new date.
            loadAvailableTimes();
        }
    );
    // Refresh available times when the party size changes.
    guestInput.addEventListener(
        "change",
        loadAvailableTimes
    );
});