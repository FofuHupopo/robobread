function loadVendingMachineList(item) {
    const vendingMachine = item.vending_machine;
        const productStock = item.product_stock;

        let table = "";

        productStock.forEach((product) => {
            table += `
                <tr>
                    <td>${product.product_name}</td>
                    <td>${product.quantity}</td>
                    <td>${product.max_quantity}</td>
                </tr>
            `;
        });

        const cardHtml = `
            <div class="card mb-4">
                <div class="card-header d-flex align-items-start">
                    <div class="d-flex justify-content-center align-items-center pe-3">
                        <span class="status-circle status-${vendingMachine.status}"></span>
                    </div>
                    <div class="flex-grow-1">
                        <h5>${vendingMachine.name}</h5>
                        <p>${vendingMachine.address}</p>
                    </div>
                    <button class="btn btn-link" id="toggleButton${vendingMachine.id}" style="cursor: pointer;">
                        <span id="toggleIcon${vendingMachine.id}" class="bi bi-chevron-down"></span>
                    </button>
                </div>

                <div class="card-body collapsed" id="cardBody${vendingMachine.id}">
                    <table class="table">
                        <thead>
                            <tr>
                                <th>Название Товара</th>
                                <th>Количество</th>
                                <th>Максимальное Количество</th>
                            </tr>
                        </thead>
                        <tbody>
                            ${table}
                        </tbody>
                    </table>
                </div>
            </div>

        `;

        return cardHtml;
}


function addListEventListener(id) {
    const button = document.getElementById(`toggleButton${id}`)

        button.addEventListener('click', function() {
            const cardBody = document.getElementById(`cardBody${id}`);
            const toggleIcon = document.getElementById(`toggleIcon${id}`);
    
            if (cardBody.classList.contains('collapsed')) {
                cardBody.classList.remove('collapsed');
                toggleIcon.classList.remove('bi-chevron-down');
                toggleIcon.classList.add('bi-chevron-up');
            } else {
                cardBody.classList.add('collapsed');
                toggleIcon.classList.remove('bi-chevron-up');
                toggleIcon.classList.add('bi-chevron-down');
            }
        });
}


document.addEventListener('DOMContentLoaded', async () => {
    async function loadProductStock() {
        const data = await getRequest('statistics/product-stock/all');

        const vendingMachineList = document.getElementById('vendingMachineList');
        vendingMachineList.innerHTML = "";

        data.forEach((item) => {
            vendingMachineList.innerHTML += loadVendingMachineList(item);
        });

        data.forEach((item) => {
            const vendingMachine = item.vending_machine;
            addListEventListener(vendingMachine.id);
        })
    }

    await loadProductStock();
});
