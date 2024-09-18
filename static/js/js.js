// myapp/static/myapp/js/script.js

document.addEventListener('DOMContentLoaded', function() {
    let currentUser = {
        name: '',
        avatar: '',
        isAdmin: false
    };

    function showAdminLogin() {
        document.getElementById('admin-login').style.display = 'block';
    }

    function closeAdminLogin() {
        document.getElementById('admin-login').style.display = 'none';
    }

    function checkAdminKey() {
        const key = document.getElementById('admin-key').value;
        if (key === 'luftwaffe') {
            currentUser.isAdmin = true;
            currentUser.name += '_moderator';
        }
        closeAdminLogin();
    }

    function addReview() {
        const usernameInput = document.getElementById('username');
        const reviewTextInput = document.getElementById('review-text');
        const avatarInput = document.getElementById('avatar');

        if (usernameInput.value === '' || reviewTextInput.value === '') {
            alert('Пожалуйста, заполните все поля');
            return;
        }

        currentUser.name = usernameInput.value;
        currentUser.avatar = avatarInput.files.length > 0 ? URL.createObjectURL(avatarInput.files[0]) : '';

        const reviewsContainer = document.getElementById('reviews');
        const reviewDiv = document.createElement('div');
        reviewDiv.className = 'review';

        const headerDiv = document.createElement('div');
        headerDiv.className = 'header';

        const nameSpan = document.createElement('span');
        nameSpan.className = 'name';
        nameSpan.innerText = currentUser.name;

        const timeSpan = document.createElement('span');
        timeSpan.className = 'time';
        timeSpan.innerText = new Date().toLocaleString();

        headerDiv.appendChild(nameSpan);
        headerDiv.appendChild(timeSpan);

        const contentDiv = document.createElement('div');
        contentDiv.className = 'content';
        contentDiv.innerText = reviewTextInput.value;

        const actionsDiv = document.createElement('div');
        actionsDiv.className = 'actions';

        const likeButton = document.createElement('button');
        likeButton.innerText = '👍 0';
        likeButton.onclick = () => {
            likeButton.innerText = `👍 ${parseInt(likeButton.innerText.split(' ')[1]) + 1}`;
        };

        const dislikeButton = document.createElement('button');
        dislikeButton.innerText = '👎 0';
        dislikeButton.onclick = () => {
            dislikeButton.innerText = `👎 ${parseInt(dislikeButton.innerText.split(' ')[1]) + 1}`;
        };

        actionsDiv.appendChild(likeButton);
        actionsDiv.appendChild(dislikeButton);

        reviewDiv.appendChild(headerDiv);
        reviewDiv.appendChild(contentDiv);
        reviewDiv.appendChild(actionsDiv);

        if (currentUser.isAdmin) {
            reviewDiv.style.float = 'right';
        } else {
            reviewDiv.style.float = 'left';
        }

        reviewsContainer.appendChild(reviewDiv);

        reviewTextInput.value = '';
    }

    document.querySelectorAll('.close').forEach(button => {
        button.onclick = () => {
            button.parentElement.parentElement.style.display = 'none';
        };
    });
});
