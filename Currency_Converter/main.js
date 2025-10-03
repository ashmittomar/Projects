// WARNING: NEVER expose your API key directly in client-side code in a production environment.
// Use a secure backend proxy to protect it.
const API_KEY = "cur_live_Edx2mQ8QcMwulMPMhthaeyLE60z4FywD9OhpIauz";
const API_URL_BASE = "https://api.currencyapi.com/v3/latest";

// ==========================================================
// 1. TAB FUNCTIONALITY
// ==========================================================

const navLinks = document.querySelectorAll(".nav-link");
const tabContents = document.querySelectorAll(".tab-content");

/**
 * Switches the active content tab and highlights the correct navigation link.
 * @param {string} tabId - The ID of the tab content to show (e.g., 'converter', 'rates', 'about').
 */
const switchTab = (tabId) => {
    // 1. Deactivate all nav links and content
    navLinks.forEach(link => link.classList.remove('active'));
    tabContents.forEach(content => content.classList.remove('active-tab'));
    
    // 2. Activate the selected nav link
    const activeLink = document.querySelector(`.nav-link[data-tab="${tabId}"]`);
    if (activeLink) {
        activeLink.classList.add('active');
    }

    // 3. Activate the selected content
    const activeContent = document.getElementById(tabId);
    if (activeContent) {
        activeContent.classList.add('active-tab');
    }
}

// Attach event listeners to all navigation links
navLinks.forEach(link => {
    link.addEventListener('click', (e) => {
        e.preventDefault();
        const tabId = e.currentTarget.getAttribute('data-tab');
        switchTab(tabId);
    });
});

// Set the default tab on load (optional, but good practice)
switchTab('converter'); 


// ==========================================================
// 2. CURRENCY CONVERTER FUNCTIONALITY (from original project)
// ==========================================================

const populateConverter = async (amount, baseCurrency) => {
    // This is the conversion function for the 'Converter' tab
    const url = `${API_URL_BASE}?apikey=${API_KEY}&base_currency=${baseCurrency}`;

    try {
        const response = await fetch(url);
        if (!response.ok) {
            throw new Error(`API call failed with status: ${response.status}`);
        }
        
        const rJson = await response.json();
        
        const tableBody = document.querySelector("#converter .output tbody");
        document.querySelector("#converter .output").style.display = "block";
        
        let tableRowsHTML = "";
        
        for (const key in rJson.data) {
            if (rJson.data.hasOwnProperty(key)) {
                const currencyData = rJson.data[key];
                const convertedValue = currencyData.value * amount;
                
                tableRowsHTML += `
                    <tr>
                        <td>${currencyData.code}</td>
                        <td>${currencyData.code}</td>
                        <td>${convertedValue.toFixed(4)}</td>
                    </tr>
                `;
            }
        }
        
        tableBody.innerHTML = tableRowsHTML;

    } catch (error) {
        console.error("Conversion failed:", error);
        const tableBody = document.querySelector("#converter .output tbody");
        document.querySelector("#converter .output").style.display = "block";
        tableBody.innerHTML = `<tr><td colspan="3" style="color: red; text-align: center;">Error: Failed to fetch currency rates. Please check console.</td></tr>`;
    }
};

const conversionForm = document.getElementById("conversionForm");
conversionForm.addEventListener("submit", (e) => {
    e.preventDefault();
    const amount = parseFloat(document.getElementById("quantity").value);
    const baseCurrency = document.getElementById("currency").value;
    
    if (isNaN(amount) || amount <= 0) {
        alert("Please enter a valid amount greater than 0.");
        return;
    }
    
    populateConverter(amount, baseCurrency);
});


// ==========================================================
// 3. LIVE RATES FUNCTIONALITY ('rates' tab)
// ==========================================================

const ratesBtn = document.querySelector(".rates-btn");
const ratesTableBody = document.querySelector("#ratesTable tbody");
const baseCurrencyDisplay = document.getElementById("baseCurrencyDisplay");
const ratesOutput = document.querySelector(".rates-output");

const fetchRates = async (baseCurrency) => {
    const url = `${API_URL_BASE}?apikey=${API_KEY}&base_currency=${baseCurrency}`;
    
    ratesOutput.style.display = "block"; // Show output area
    ratesTableBody.innerHTML = '<tr><td colspan="3" style="text-align: center; color: var(--primary-color);">Fetching live rates...</td></tr>';
    baseCurrencyDisplay.textContent = baseCurrency;

    try {
        const response = await fetch(url);
        if (!response.ok) {
            throw new Error(`API call failed with status: ${response.status}`);
        }
        
        const rJson = await response.json();
        let tableRowsHTML = "";
        let count = 0;

        // Display only top 15 currencies for a clean look
        for (const key in rJson.data) {
             if (rJson.data.hasOwnProperty(key) && count < 15) {
                const currencyData = rJson.data[key];
                
                // Rate is simply the value, as the base is 1 unit
                tableRowsHTML += `
                    <tr>
                        <td>${currencyData.code}</td>
                        <td>${currencyData.code}</td>
                        <td>${currencyData.value.toFixed(4)}</td>
                    </tr>
                `;
                count++;
            }
        }
        
        ratesTableBody.innerHTML = tableRowsHTML;

    } catch (error) {
        console.error("Rates fetch failed:", error);
        ratesTableBody.innerHTML = `<tr><td colspan="3" style="color: red; text-align: center;">Error: Could not fetch live rates.</td></tr>`;
    }
}

// Event listener for the Live Rates button
ratesBtn.addEventListener("click", () => {
    const baseCurrency = document.getElementById("baseRateCurrency").value;
    fetchRates(baseCurrency);
});

// Automatically fetch rates for a default currency when the script runs
document.addEventListener('DOMContentLoaded', () => {
    fetchRates(document.getElementById("baseRateCurrency").value);
});