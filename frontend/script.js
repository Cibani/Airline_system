document.getElementById("songForm").addEventListener("submit", function(e) {
    e.preventDefault();
    alert("In real app, this will send data to Java backend!");
});

window.onload = function() {
    document.getElementById("songList").innerHTML = "<p>List of songs will appear here</p>";
};
