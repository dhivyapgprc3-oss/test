document.addEventListener("DOMContentLoaded", () => {
	const tbody = document.getElementById("table-body");

	async function loadTable() {
		try {
			const response = await fetch("/api/table", { headers: { "Accept": "application/json" } });
			if (!response.ok) throw new Error(`HTTP ${response.status}`);
			const payload = await response.json();
			const rows = payload.rows || [];

			tbody.innerHTML = "";
			for (const row of rows) {
				const tr = document.createElement("tr");
				const tdLeft = document.createElement("td");
				const tdRight = document.createElement("td");
				tdLeft.textContent = row.col_left;
				tdRight.textContent = row.col_right;
				tr.appendChild(tdLeft);
				tr.appendChild(tdRight);
				tbody.appendChild(tr);
			}
		} catch (error) {
			console.error("Failed to load table:", error);
			tbody.innerHTML = `<tr><td colspan="2">Failed to load data.</td></tr>`;
		}
	}

	loadTable();
});