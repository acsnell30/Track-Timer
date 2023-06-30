var button_1 = $("#start_run");
button_1.click(function() {
    console.log(button_1.text());
    if (button_1.text() === "Start") {
        $('#result').text("Run In Progress...");
        $.ajax({
            url: "/start_run",
            type: "post",
            success: function(response) {
                console.log(response);
                $('#result').text(response);
            }
        });
    } else {
        $('#result').text("Run In Progress...");
        $.ajax({
            url: "/start_run",
            type: "post",
            success: function(response) {
                console.log(response);
                $('#result').text(response);
            }
        })
    }
});

var button_2 = $("#reset_run");
button_2.click(function() {
    console.log(button_2.text());
    if (button_2.text() === "Reset") {
        $.ajax({
            url: "/reset_run",
            type: "post",
            success: function(response) {
                console.log(response);
                $('#result').text("");
            }
        });
    } else {
        $.ajax({
            url: "/reset_run",
            type: "post",
            success: function(response) {
                console.log(response);
                $('#result').text("");
            }
        })
    }
});
