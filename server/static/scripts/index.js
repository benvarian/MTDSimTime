$(document).ready(function () {
    console.log("JS Loaded");

    // Submit the form via AJAX
    $(".simulation-form").submit(function (event) {
        event.preventDefault();

        console.log("Form submitted via AJAX");

        $.ajax({
            url: '/run_simulation',
            type: 'POST',
            data: $(this).serialize(),
            success: function (response) {
                $("#networkPlot").attr("src", response.image_url).show();
            }
        });
    });

    // Trigger form submission on button click
    $("#startSimulation").click(function () {
        $(".simulation-form").submit();
    });
});
