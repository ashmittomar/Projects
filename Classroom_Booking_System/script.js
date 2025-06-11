const form = document.getElementById("bookingForm");
const tableBody = document.querySelector("#bookingTable tbody");

form.addEventListener("submit", function (e) {
  e.preventDefault();

  const teacherName = document.getElementById("teacherName").value.trim();
  const subject = document.getElementById("subject").value.trim();
  const date = document.getElementById("date").value;
  const time = document.getElementById("time").value;
  const classroom = document.getElementById("classroom").value;

  if (!teacherName || !subject || !date || !time || !classroom) {
    alert("Please fill in all fields.");
    return;
  }

  const newRow = document.createElement("tr");

  newRow.innerHTML = `
    <td>${date}</td>
    <td>${time}</td>
    <td>${classroom}</td>
    <td>${subject}</td>
    <td>${teacherName}</td>
  `;

  tableBody.appendChild(newRow);
  form.reset();
});
