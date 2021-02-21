var URL = "/asset/filter/";
var query = new Map();

$(document).ready(
    function() {
        $.getJSON(URL,{},showRecords);
    }
);

(function($) {
    $.fn.onEnter = function(func) {
        this.bind('keypress', function(e) {
            if (e.keyCode == 13) func.apply(this, [e]);
        });
        return this;
     };
})(jQuery);

$( function () {
    $("input").onEnter( function() {
        getRecords(1);
    });
});

function getRecords(page_no) {
    query.set("device_id", $("#device_filter").val());
    query.set("name", $("#name_filter").val());
    query.set("description", $("#desc_filter").val());
    query.set("status", $("#status_filter").val());
    query.set("note", $("#note_filter").val());

    var first = true;
    url = URL;
    for (const [key, value] of query.entries()) {
        if (value) {
            if (first == true) {
                url += "?";
                first = false;
            } else {
                url += "&";
            }
            url += key + "=" + value;
        }
    }
    if (first == true) {
        url += "?"
    } else {
        url += "&"
    }
    url += "page=" + page_no;
    $.getJSON(url,{},showRecords);
}

// Render the table's row in table request-table
function render_table_rows(rows, page_size, page_no) {
    $("#recordrows").empty();
    $.each(rows, function(idx,row) {
        $("#recordrows").append("<tr><td><div class=\"cell\">" +
            row.device_id + "</div></td><td><div class=\"cell\">" +
            row.name + "</div></td><td><div class=\"cell\">" +
            row.description + "</div></td><td><div class=\"cell\">" +
            row.quantity + "</div></td><td><div class=\"cell\">" +
            row.status + "</div></td><td><div class=\"cell\">" +
            row.license + "</div></td><td><div class=\"cell\">" +
            row.management + "</div></td><td><div class=\"cell\">" +
            row.note + "</div></td></tr>");
        }
    );
}


function showRecords(pages) {
    //calling pagination function
    pagination(pages);
    render_table_rows(pages.results);
}

function pagination(pages) {
    $("#pages").empty();
    $("#pages").append("<li class=\"page-item active\"><a class=\"page-link\">Count: " + pages.results.length + "/" + pages.total + "</a></li>");
    if (pages.previous) {
        $("#pages").append("<li class=\"page-item\"><a class=\"page-link\" onclick=getRecords(" + pages.previous_page_number + ")>Prev</a></li>");
    } else {
        $("#pages").append("<li class=\"page-item disabled\"><a class=\"page-link\">Prev</a></li>");
    }
    for (var i = 1; i <= pages.page_range.length; i++) {
        if (pages.number == i) {
            $("#pages").append("<li class=\"page-item active\"><a class=\"page-link\">" + i + "</a></li>");
        } else {
            $("#pages").append("<li class=\"page-item\"><a class=\"page-link\" onclick=getRecords(" + i + ")>" + i + "</a></li>");
        }
    }
    if (pages.next) {
        $("#pages").append("<li class=\"page-item\"><a class=\"page-link\" onclick=getRecords(" + pages.next_page_number + ")>Next</a></li>");
    } else {
        $("#pages").append("<li class=\"page-item disabled\"><a class=\"page-link\">Next</a></li>");
    }
}