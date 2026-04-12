async function findRoute() {
    const source = document.getElementById("source").value;
    const destination = document.getElementById("destination").value;
    const pref = document.getElementById("preference").value;

    const res = await fetch(`http://127.0.0.1:5000/route?source=${source}&destination=${destination}&preference=${pref}`);
    const data = await res.json();

    if (data.message) {
        document.getElementById("result").innerText = data.message;
    } else {
        document.getElementById("result").innerText =
            `Best Route: ${data.mode} | Time: ${data.time} hrs | Cost: ₹${data.cost}`;
    }
}
