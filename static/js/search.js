$(document).ready(function() {
    $('#search-input').keyup(function() {
        var query = $(this).val();
        if (query.length > 0) {
            $.ajax({
                url: '/search/',  // Убедитесь, что URL совпадает с тем, что вы настроили в urls.py
                data: {'query': query},
                success: function(data) {
                    var dropdown = $('#search-dropdown');
                    dropdown.empty();
                    if (data.results.length > 0) {
                        $.each(data.results, function(index, obj) {
                            dropdown.append(
                                '<li class="dropdown-item">' +
                                '<img src="' + obj.photo_url + '" alt="" style="width: 50px; height: 50px; margin-right: 10px;">' +
                                obj.name +
                                '</li>'
                            );
                        });
                    } else {
                        dropdown.append('<li class="dropdown-item">Ничего не найдено</li>');
                    }
                    dropdown.show();
                }
            });
        } else {
            $('#search-dropdown').hide();
        }
    });
});
