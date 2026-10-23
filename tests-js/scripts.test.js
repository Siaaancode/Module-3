/**
 * @jest-environment jsdom
 */

async function flushPromises() {
    await Promise.resolve();
    await Promise.resolve();
    await Promise.resolve();
}

describe("Kokoro booking calendar", function () {
    let calendarOptions;
    let calendarRender;

    beforeEach(function () {
        // Set up the HTML elements used by scripts.js.
        document.body.innerHTML = `
            <div id="calendar"></div>
            <p id="selected-date"></p>
            <input id="booking_date" type="date">
            <input id="guests" type="number" value="2">
            <select id="booking_time" disabled></select>
        `;

        // Mock FullCalendar so the real library is not required.
        calendarRender = jest.fn();

        global.FullCalendar = {
            Calendar: jest.fn(function (element, options) {
                calendarOptions = options;

                return {
                    render: calendarRender
                };
            })
        };

        // Prevent requests from reaching a real server.
        global.fetch = jest.fn();

        // Load the script afresh for each test.
        jest.resetModules();
        require("../bookings/static/js/scripts.js");

        // Trigger the script's initialisation.
        document.dispatchEvent(
            new Event("DOMContentLoaded")
        );
    });

    afterEach(function () {
        jest.restoreAllMocks();
        delete global.FullCalendar;
        delete global.fetch;
    });

    test("initialises and renders the calendar", function () {
        expect(global.FullCalendar.Calendar)
            .toHaveBeenCalled();

        expect(calendarRender).toHaveBeenCalled();
    });

    test("selecting a date updates the date input and text", function () {
        const dateCell = document.createElement("div");

        // Simulate selecting a calendar date.
        calendarOptions.dateClick({
            dateStr: "2026-10-25",
            dayEl: dateCell
        });

        expect(
            document.getElementById("booking_date").value
        ).toBe("2026-10-25");

        expect(
            document.getElementById("selected-date").textContent
        ).toBe("Selected date: 2026-10-25");

        expect(dateCell.classList.contains("selected-date-cell"))
            .toBe(true);
    });

    test("does not initialise when required elements are missing", function () {
        // Remove a required element before initialisation.
        document.getElementById("guests").remove();

        jest.resetModules();
        global.FullCalendar.Calendar.mockClear();

        require("../bookings/static/js/scripts.js");

        document.dispatchEvent(
            new Event("DOMContentLoaded")
        );

        expect(global.FullCalendar.Calendar)
            .not.toHaveBeenCalled();
    });

    test("loads available booking times successfully", async function () {
        const dateInput = document.getElementById("booking_date");
        const timeInput = document.getElementById("booking_time");

        // Mock a successful response from the availability endpoint.
        global.fetch.mockResolvedValue({
            ok: true,
            json: jest.fn().mockResolvedValue({
                times: [
                    { label: "12:00 pm", value: "12:00" },
                    { label: "12:30 pm", value: "12:30" }
                ]
            })
        });

        // Simulate selecting a date on the calendar.
        calendarOptions.dateClick({
            dateStr: "2026-10-25",
            dayEl: document.createElement("div")
        });

        // Wait for fetch and JSON parsing to complete.
        await flushPromises();

        expect(global.fetch).toHaveBeenCalled();

        // Check that the available times were added to the dropdown.
        expect(
            Array.from(timeInput.options).map(function (option) {
                return option.value;
            })
        ).toEqual(["", "12:00", "12:30"]);

        // Check that the dropdown is enabled.
        expect(timeInput.disabled).toBe(false);
    });

    test("displays a message when no booking times are available", async function () {
        global.fetch.mockResolvedValue({
            ok: true,
            json: jest.fn().mockResolvedValue({
                times: []
            })
        });

        calendarOptions.dateClick({
            dateStr: "2026-10-25",
            dayEl: document.createElement("div")
        });

        await flushPromises();

        const timeInput = document.getElementById("booking_time");

        expect(timeInput.options[0].textContent)
            .toBe("No times available");

        expect(timeInput.disabled).toBe(true);
    });


    test("displays an error message when the request fails", async function () {
        jest.spyOn(console, "error").mockImplementation(function () { });

        global.fetch.mockRejectedValue(
            new Error("Network error")
        );

        calendarOptions.dateClick({
            dateStr: "2026-10-25",
            dayEl: document.createElement("div")
        });

        await flushPromises();

        const timeInput = document.getElementById("booking_time");

        expect(timeInput.options[0].textContent)
            .toBe("Unable to load times. Try again.");
    });


    test("reloads availability when the guest count changes", async function () {
        global.fetch.mockResolvedValue({
            ok: true,
            json: jest.fn().mockResolvedValue({
                times: [
                    { label: "12:00 pm", value: "12:00" }
                ]
            })
        });

        const dateInput = document.getElementById("booking_date");
        const guestInput = document.getElementById("guests");

        dateInput.value = "2026-10-25";
        guestInput.value = "4";

        guestInput.dispatchEvent(new Event("change"));

        await flushPromises();

        expect(global.fetch).toHaveBeenCalled();

        const requestUrl = new URL(global.fetch.mock.calls[0][0]);

        expect(requestUrl.searchParams.get("date"))
            .toBe("2026-10-25");

        expect(requestUrl.searchParams.get("guests"))
            .toBe("4");
    });


    test("prompts the customer to select a date when no date is selected", function () {
        const dateInput = document.getElementById("booking_date");
        const timeInput = document.getElementById("booking_time");

        // Simulate clearing the selected date.
        dateInput.value = "";
        dateInput.dispatchEvent(new Event("change"));

        expect(timeInput.options[0].textContent)
            .toBe("Select a date");

        expect(timeInput.disabled).toBe(true);

        expect(global.fetch).not.toHaveBeenCalled();
    });


    test("disables the dropdown while availability is loading", async function () {
        let resolveFetch;

        // Keep the request pending so the loading state can be checked.
        global.fetch.mockReturnValue(
            new Promise(function (resolve) {
                resolveFetch = resolve;
            })
        );

        calendarOptions.dateClick({
            dateStr: "2026-10-25",
            dayEl: document.createElement("div")
        });

        const timeInput = document.getElementById("booking_time");

        // Check the dropdown before the request has completed.
        expect(timeInput.options[0].textContent)
            .toBe("Checking availability...");

        expect(timeInput.disabled).toBe(true);

        // Complete the request so the test leaves no pending work.
        resolveFetch({
            ok: true,
            json: jest.fn().mockResolvedValue({
                times: [
                    { label: "12:00 pm", value: "12:00" }
                ]
            })
        });

        await flushPromises();

        expect(timeInput.disabled).toBe(false);
    });

});