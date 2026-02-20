const EXCLUDED_FOLDERS = ["qrcode", "venv", "nomCanyon", "assets", "img", "css", "js"];

async function loadCanyons() {
    const container = document.getElementById("links-container");
    try {
        const response = await fetch("https://api.github.com/repos/40ansEFC/traceGPX/contents/");

        if (!response.ok) {
            throw new Error(`Erreur réseau: ${response.status}`);
        }

        const data = await response.json();

        const validFolders = data
            .filter((item) => item.type === "dir" && !item.name.startsWith(".") && !EXCLUDED_FOLDERS.includes(item.name))
            .map((item) => item.name);

        validFolders.sort();

        if (validFolders.length === 0) {
            container.innerHTML = '<div class="loading">Aucun parcours trouvé.</div>';
            return;
        }

        let linksHtml = "";
        for (const folder of validFolders) {
            const words = folder.split("-");
            const displayName = words.map((word) => word.charAt(0).toUpperCase() + word.slice(1)).join(" ");

            const lastWord = words[words.length - 1].toLowerCase();
            let icon = "📍"; // Pin pour les autres

            if (lastWord === "acces" || lastWord === "accès") {
                icon = "<span style='display:inline-block; transform: scaleX(-1);'>🚶</span>"; // Inversé (droite)
            } else if (lastWord === "retour") {
                icon = "🚶"; // Défaut (gauche)
            }

            linksHtml += `<a href="./${folder}/" class="btn btn-block">${icon} ${displayName}</a>\n`;
        }

        container.innerHTML = linksHtml;
    } catch (error) {
        console.error("Erreur lors du chargement des dossiers:", error);
        container.innerHTML = `
            <div class="error">
                Impossible de charger les parcours automatiquement.<br>
                Veuillez réessayer plus tard ou vérifier votre connexion.<br>
                <small style="opacity:0.7">(${error.message})</small>
            </div>`;
    }
}

function filterCanyons() {
    const searchInput = document.getElementById("search-input").value.toLowerCase();
    const links = document.querySelectorAll("#links-container .btn");
    let hasVisible = false;

    links.forEach((link) => {
        const text = link.textContent.toLowerCase();
        if (text.includes(searchInput)) {
            link.style.display = "block";
            hasVisible = true;
        } else {
            link.style.display = "none";
        }
    });

    // Gérer l'affichage d'un message "Aucun résultat"
    let noResultsMsg = document.getElementById("no-results-msg");
    if (!hasVisible && links.length > 0) {
        if (!noResultsMsg) {
            noResultsMsg = document.createElement("div");
            noResultsMsg.id = "no-results-msg";
            noResultsMsg.className = "loading";
            noResultsMsg.textContent = "Aucun parcours ne correspond à votre recherche.";
            document.getElementById("links-container").appendChild(noResultsMsg);
        }
        noResultsMsg.style.display = "block";
    } else if (noResultsMsg) {
        noResultsMsg.style.display = "none";
    }
}

document.addEventListener("DOMContentLoaded", loadCanyons);
