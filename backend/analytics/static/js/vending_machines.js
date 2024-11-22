async function loadVendingMachines() {
    const data = await getRequest('vending-machines/vending-machine')

    const vendingMachineList = $('#vendingMachineList');
    vendingMachineList.empty();

    function formatDate(utcString) {
        const date = new Date(utcString);

        return date.toLocaleString('ru-RU', {
            year: 'numeric',
            month: 'long',
            day: 'numeric',
            hour: '2-digit',
            minute: '2-digit',
            second: '2-digit'
        });
    }

    data.forEach((machine) => {
        vendingMachineList.append(`
            <tr>
                <td>${machine.name}</td>
                <td>${machine.address}</td>
                <td>${machine.ip_address}</td>
                <td>
                    <div class="d-flex justify-content-center align-items-center">
                        <span class="status-circle status-${machine.status}"></span>
                    </div>
                </td>
                <td>${formatDate(machine.last_sync_date)}</td>
                <td>
                    <button class="btn btn-danger" onclick="deleteVendingMachine(${machine.id})">Удалить</button>
                </td>
            </tr>
        `);
    });
}

const deleteVendingMachine = async (id) => {
    await deleteRequest(`vending-machines/vending-machine/${id}`);
    await loadVendingMachines();
}

$(document).ready(async () => {
    await loadVendingMachines();

    $('#addVendingMachineForm').on('submit', async (e) => {
        e.preventDefault();

        const newMachine = {
            ip_address: $('#ip_address').val()
        };

        const data = await postRequest('vending-machines/vending-machine', newMachine);
        console.log(data)

        $('#addVendingMachineForm')[0].reset();
        await loadVendingMachines();
    });
});
