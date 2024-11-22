const apiUrl = 'http://127.0.0.1:8004/api';


async function getRequest(subUrl) {
    try {
        const response = await fetch(`${apiUrl}/${subUrl}`);
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        const data = await response.json();
        console.log('GET response:', data);
        return data;
    } catch (error) {
        console.error('There was a problem with the fetch operation:', error);
    }
}

async function postRequest(subUrl, newItem) {
    try {
        const response = await fetch(`${apiUrl}/${subUrl}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(newItem),
            credentials: 'omit',
        });
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        const data = await response.json();
        console.log('POST response:', data);
        return data;
    } catch (error) {
        console.error('There was a problem with the fetch operation:', error);
    }
}

async function putRequest(subUrl, updatedItem) {
    try {
        const response = await fetch(`${apiUrl}/${subUrl}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(updatedItem),
        });
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        const data = await response.json();
        console.log('PUT response:', data);
        return data;
    } catch (error) {
        console.error('There was a problem with the fetch operation:', error);
    }
}

async function deleteRequest(subUrl) {
    try {
        const response = await fetch(`${apiUrl}/${subUrl}`, {
            method: 'DELETE',
        });
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        const data = await response.json()
        console.log('DELETE response:', data);
        return data;
    } catch (error) {
        console.error('There was a problem with the fetch operation:', error);
    }
}
