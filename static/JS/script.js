// Make sidebar menu items active when clicked
function setActive(element) {
    document.querySelectorAll(".sidebar-item").forEach((item) => item.classList.remove("bg-blue-700"));
    element.parentElement.classList.add("bg-blue-700");
}

// Fetch stock data and render the graph
async function loadStockChart() {
    const ctx = document.getElementById("stockChart").getContext("2d");

    // Dummy stock data (replace with API data)
    const stockData = {
        labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
        datasets: [{
            label: "Stock Price",
            data: [120, 130, 125, 140, 150, 160],
            borderColor: "blue",
            borderWidth: 2
        }]
    };

    new Chart(ctx, {
        type: "line",
        data: stockData
    });
}

loadStockChart();

// Fetch and display news
async function fetchNews() {
    const newsContainer = document.getElementById("news-container");
    newsContainer.innerHTML = "<p>Loading news...</p>";

    try {
        const response = await fetch("https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=YOUR_API_KEY");
        const data = await response.json();
        
        newsContainer.innerHTML = ""; // Clear old news

        data.articles.forEach((article) => {
            let newsItem = `<div class="p-4 border-b border-gray-200">
                <h3 class="text-lg font-semibold">${article.title}</h3>
                <p class="text-gray-600">${article.description}</p>
                <a href="${article.url}" target="_blank" class="text-blue-500 hover:underline">Read More</a>
            </div>`;
            newsContainer.innerHTML += newsItem;
        });

    } catch (error) {
        newsContainer.innerHTML = "<p class='text-red-500'>Error loading news.</p>";
        console.error("Error fetching news:", error);
    }
}

fetchNews();
