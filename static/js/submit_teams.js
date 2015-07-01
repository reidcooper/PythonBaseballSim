$(function() {
    $('#btnCreateTeams').click(function() {

        var home_team = $('#selectHomeTeam').val();
        var away_team = $('#selectAwayTeam').val();

        $.ajax({
            url: '/submitTeams',
            data: JSON.stringify({myDict: {selectHomeTeam: home_team, selectAwayTeam: away_team}}),
            type: 'POST',
            contentType: "application/json; charset=utf-8",
            dataType: "json",
            success: function(response) {
                console.log(response);
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});