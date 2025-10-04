const form = document.getElementById("bookingForm");
const tableBody = document.querySelector("#bookingTable tbody");
const clearButton = document.getElementById("clearBookingsButton");

// Array to store booking data for easy conflict checking and sorting
let bookedSlots = [];

/**
 * Sorts the bookedSlots array first by Date, then by Time.
 */
function sortBookings() {
    bookedSlots.sort((a, b) => {
        // First, compare by Date
        const dateA = new Date(a.date);
        const dateB = new Date(b.date);
        if (dateA - dateB !== 0) {
            return dateA - dateB;
        }

        // If dates are equal, compare by Time (lexicographically, which works for HH:MM format)
        if (a.time < b.time) return -1;
        if (a.time > b.time) return 1;
        return 0;
    });
}

/**
 * Renders the bookedSlots array to the DOM table.
 */
function renderBookings() {
    tableBody.innerHTML = ''; // Clear existing rows
    sortBookings(); // Sort before rendering

    bookedSlots.forEach(slot => {
        const newRow = document.createElement("tr");
        newRow.innerHTML = `
            <td>${slot.date}</td>
            <td>${slot.time}</td>
            <td>${slot.classroom}</td>
            <td>${slot.subject}</td>
            <td>${slot.teacherName}</td>
        `;
        tableBody.appendChild(newRow);
    });
}

/**
 * Checks if a proposed booking conflicts with existing ones.
 */
function isConflict(date, time, classroom) {
  return bookedSlots.some(slot =>
    slot.date === date &&
    slot.time === time &&
    slot.classroom === classroom
  );
}

// --- Event Listeners ---

form.addEventListener("submit", function (e) {
  e.preventDefault();

  const teacherName = document.getElementById("teacherName").value.trim();
  const subject = document.getElementById("subject").value.trim();
  const date = document.getElementById("date").value;
  const time = document.getElementById("time").value;
  const classroom = document.getElementById("classroom").value;

  if (!teacherName || !subject || !date || !time || !classroom) {
    alert("❌ Error: Please ensure all booking fields are completed.");
    return;
  }
    
  if (isConflict(date, time, classroom)) {
    alert(`⚠️ Booking Conflict: Classroom ${classroom} is already reserved for ${date} at ${time}.`);
    return;
  }

  // Create the new booking object
  const newBooking = { teacherName, subject, date, time, classroom };
  bookedSlots.push(newBooking);

  // Render the updated and sorted list
  renderBookings(); 

  // Success message and form reset
  alert(`✅ Success! ${classroom} booked for ${subject} on ${date}.`);
  form.reset();
});


clearButton.addEventListener("click", function() {
    if (bookedSlots.length === 0) {
        alert("The booking schedule is already empty.");
        return;
    }
    
    // Professional confirmation dialog
    const confirmation = confirm("🚨 WARNING: Are you sure you want to clear ALL existing bookings? This action cannot be undone.");
    
    if (confirmation) {
        bookedSlots = []; // Empty the data array
        renderBookings(); // Render the empty array (clears the table)
        alert("🗑️ All classroom bookings have been successfully cleared.");
    }
});