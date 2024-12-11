const apiUrl = 'http://localhost:5000/api';

fetch(apiUrl)
  .then(response => {
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    return response.json();
  })
  .then(data => {
    const heading = data.heading;
    const list = data.list;

    const headingElement = document.querySelector('h1');
    headingElement.textContent = heading;

    const ul = document.createElement('ul');

    list.forEach(item => {
      const li = document.createElement('li');
      li.textContent = item;
      ul.appendChild(li);
    });

    document.body.appendChild(ul);
  })
  .catch(error => {
    console.error('Error fetching data:', error);
  });
