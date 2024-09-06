const itemsEnter = document.querySelectorAll('.count-enter');

itemsEnter.forEach(input => {
  input.addEventListener('input', function() {
    if (parseInt(this.value) > parseInt(this.getAttribute('max') || Infinity)) {
        console.log(this.getAttribute('max'), this.value)
      this.value = this.getAttribute('max') || '';
    }
  });
});

function setNotification(message, isSuccess) {
    const notification = document.getElementById("notification")
    notification.innerText = message;

    if (isSuccess) {
        notification.classList.remove('red');
        notification.classList.add('green');
    }
    else {
        notification.classList.remove('green');
        notification.classList.add('red');
    }
}

function clearNotification() {
    const notification = document.getElementById("notification")
    notification.innerText = "";
}

function fillItem(num) {
    const item = document.getElementById(`count-enter${num}`)
    item.value = item.max;
}

function removeItem(num) {
    const item = document.getElementById(`needs_to_remove${num}`)
    
    const raw_value = document.getElementById(`needs_to_remove_value${num}`)
    const value = parseInt(raw_value.innerHTML)

    const cell_count = document.getElementById(`count-enter${num}`)

    cell_count.value = cell_count.value - value;
    item.style = "display: none;"
    
    document.getElementById(`fill${num}`).disabled = false;
    
    clearNotification()
}

function allExpiredProductsRemoved() {
    for (const button of document.querySelectorAll(".fill")) {
        if (button.disabled)
            return false;
    }

    return true;
}

function fillAll() {
    console.log(allExpiredProductsRemoved())
    if (allExpiredProductsRemoved()) {
        itemsEnter.forEach(input => {
            input.value = input.max;
        })

        setNotification(
            "Товары успешно заполнены",
            true
        )
    }
    else {
        setNotification(
            "Сначала необходимо изъять все товары с истекшим сроком годности",
            false
        )
    }
}

function get_vending_machine_id() {
    const currentUrl = new URL(window.location.href)

    const path = currentUrl.pathname
    
    const parts = path.split('/')

    const id = parts[parts.length - 1]

    return parseInt(id)
}

function save() {
    const items = [];

    document.querySelectorAll('.item').forEach(item => {
        const cell = parseInt(item.classList[1].replace("item", ""));
        const count = parseInt(item.querySelector('.count-enter').value);

        let removed = 0
        const needs_to_remove_input = item.querySelector('.needs_to_remove_value')
        if (needs_to_remove_input) {
            removed = parseInt(needs_to_remove_input.innerHTML)
        }

        items.push({ cell, count, removed });
    })

    fetch("/packing-submit", {
        method: "POST",
        body: JSON.stringify({
            items,
            vending_machine_id: get_vending_machine_id()
        }),
    })
    .then(response => response.json())
    .then(data => {
        setNotification(
            "Данные обновлены",
            true
        )
    })
    .catch(error => {
        setNotification(
            "Ошибка при обновлении данных",
            false
        )
    });
}
