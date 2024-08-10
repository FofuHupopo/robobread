const itemsEnter = document.querySelectorAll('.count-enter');

itemsEnter.forEach(input => {
  input.addEventListener('input', function() {
    if (parseInt(this.value) > parseInt(this.getAttribute('max') || Infinity)) {
        console.log(this.getAttribute('max'), this.value)
      this.value = this.getAttribute('max') || '';
    }
  });
});


function fillItem(num) {
    const item = document.getElementById(`count-enter${num}`)
    item.value = item.max;
}

function fillAll() {
    itemsEnter.forEach(input => {
        input.value = input.max;
    })
}

function save() {
    const items = [];

    document.querySelectorAll('.item').forEach(item => {
        const id = parseInt(item.classList[1].replace("item", ""));
        const count = parseInt(item.querySelector('.count-enter').value);

        items.push({ id, count });
    })

    fetch("/packing-submit", {
        method: "POST",
        body: JSON.stringify({ items }),
    })
    .then(response => response.json())
    .then(data => {
        const notification = document.getElementById("notification")
        notification.innerText = "Данные обновлены";
        notification.classList.remove('red');
        notification.classList.add('green');

    })
    .catch(error => {
        const notification = document.getElementById("notification")
        notification.innerText = "Ошибка при обновлении данных";
        notification.classList.remove('green');
        notification.classList.add('red');
    });
}
