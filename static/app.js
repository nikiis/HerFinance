            // scroll to top btn
            const btnScrollToTop = document.querySelector('#btnScrollToTop');
            btnScrollToTop.addEventListener('click', function () {
                window.scrollTo({
                    top: 0,
                    left: 0,
                    behavior: 'smooth',
                });
            });

            const btns = document.querySelectorAll('.question-btn');

            btns.forEach(function (btn) {
                btn.addEventListener('click', function (e) {
                    const question =
                        e.currentTarget.parentElement.parentElement;

                    question.classList.toggle('show-text');
                });
            });

            // appending new user comment to the website
            addButton = document.getElementById('add-comment');
            commentItem = document.querySelector('.comment-item');
            commentSection = document.getElementById('comment-section');

            console.log(addButton, commentItem, commentSection);

            addButton.addEventListener('click', () => {
                newUsername = document.querySelector('input#username');
                newUserComment = document.querySelector('textarea#new-comment');

                let newElement = document.createElement('div');
                newElement.setAttribute('class', 'row mt-5');
                newElement.innerHTML = `<div class="col-2 d-flex align-items-center">
                                <i class="fas fa-user-circle fa-7x"></i>
                            </div>
                            <div class="col-10">
                                <p
                                    class="user-name"
                                    style="font-size: 2rem; letter-spacing: 2px"
                                >
                                    <b>${newUsername.value}</b>
                                </p>
                                <p
                                    class="user-comment"
                                    style="
                                        font-size: 1.2rem;
                                        letter-spacing: 1px;
                                        color: #1b3936;
                                    "
                                >
                                  ${newUserComment.value}
                                </p>
                            </div>`;

                commentSection.appendChild(newElement);
                console.log(commentSection);
            });