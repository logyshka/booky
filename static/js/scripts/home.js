const apiPrefix = 'api/books/'
const bookContainerEl = $('#books-container');
const paginationEl = $('#pagination');

$(document).ready(function () {
    let currentPage = 1;
    const pageSize = 10; // Это должно соответствовать PAGE_SIZE в Django

    function loadBooks(page) {
        $.ajax({
            url: `${apiPrefix}?page=${page}`,
            method: 'GET',
            success: function (data) {
                bookContainerEl.empty();
                paginationEl.empty();

                // Добавляем книги
                let bookHtml = '';
                data.results.forEach((book, index) => {
                    if (index % 2 === 0) {
                        if (index !== 0) {
                            bookHtml += '</div>';
                        }
                        bookHtml += '<div class="row m-3 justify-content-center gap-3">';
                    }
                    const genreBadges = book.genres.map(genre =>
                        `<span class="badge text-bg-info">${genre.name}</span>`
                    ).join(' ');

                    bookHtml += `
                        <div class="col-sm">
                            <div class="card rounded-3 shadow border-0">
                                <div class="card-body">
                                    <h4 class="card-title fw-bold">
                                        ${book.title}
                                    </h4>
                                    <h5 class="fw-light mb-3">
                                        ${book.author.fullname}
                                    </h5>
                                    <div class="mt-3 mb-1">
                                        <span class="btn btn-outline-primary">
                                            Рейтинг <span class="badge text-bg-danger">${book.rating}</span>
                                        </span>
                                    </div>
                               
                                    <h6 class="card-subtitle mb-2 mt-3 text-body-secondary">
                                        ${genreBadges}
                                    </h6>
                                    <p class="card-text fst-italic mt-3">
                                        ${book.description.substring(0, 100)}...
                                    </p>
                                    <div class="d-grid">
                                        <a href="/books/${book.id}/" class="btn btn-primary mt-3 btn">More info</a>
                                    </div>
                                </div>
                            </div>
                        </div>
                    `;
                });


                if (data.results.length > 0) {
                    bookHtml += '</div>'; // Закрываем последний ряд
                }
                bookContainerEl.append(bookHtml);

                // Добавляем пагинацию
                const totalPages = Math.ceil(data.count / pageSize);
                for (let i = 1; i <= totalPages; i++) {
                    paginationEl.append(`
                        <li class="page-item ${i === currentPage ? 'active' : ''}">
                            <a class="page-link" href="#" data-page="${i}">${i}</a>
                        </li>
                    `);
                }
            }
        });
    }

    loadBooks(currentPage);

    // Обработка кликов по пагинации
    $(document).on('click', '#pagination .page-link', function (e) {
        e.preventDefault();
        currentPage = $(this).data('page');
        loadBooks(currentPage);
    });
});
