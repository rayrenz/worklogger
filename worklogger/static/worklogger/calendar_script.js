var active = new Date();
var view = new Date();
var month = new Date().getMonth();
var year = new Date().getFullYear();
view.setDate(1);

var months = [ 'January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December'];



// returns the current date in format yyyy-mm-dd
function getDate(){
    var yyyy = active.getFullYear().toString();
    var mm = active.getMonth() + 1;
    mm = (mm < 10) ? '0' + mm.toString() : mm.toString();
    var dd = active.getDate();
    dd = (dd < 10) ? '0' + dd.toString() : dd.toString();
    return yyyy + '-' + mm + '-' + dd;
}

// set the dates on the calendar based on the current month and year
function setDates(){
    var number_of_days = new Date(year, month + 1, 0).getDate();
    view.setMonth(month);
    view.setFullYear(year);

    var dates = ''

    for(var i = 0; i < view.getDay(); i++){
        dates += '<div>&nbsp;</div>';
    }

    for(var i = 1; i <= number_of_days; i++){
        dates += '<div class="day' + i + '"><button>' + i + '</button></div>';
    }
    $('.dates').html(dates);
}

// add class active to the current day
function setActive(){
    var i = active.getDate();
    if(view.getFullYear() == active.getFullYear() && view.getMonth() == active.getMonth()){
        $('.day' + i).addClass('active');
    }
}

function setMonthYear(){
    $('.current_year').text(view.getFullYear());
    $('.current_month').text(months[view.getMonth()]);
}

$(document).ready(function(){
    // set logdate value to current date
    $('.logdate').val(getDate());

    // set the month and year
    setMonthYear();
    // populate the dates
    setDates();
    // set the cuerent day
    setActive();

    // go next month
    $('.next').click(function(){
        month += 1;
        if(month == 12){
            year += 1;
            month = 0;
        }
        view.setMonth(month);
        view.setFullYear(year);
        setDates();
        setMonthYear();
        setActive();
    });

    // view previous month
    $('.prev').click(function(){
        month -= 1;
        if(month == -1){
            year -= 1;
            month = 11;
        }
        view.setMonth(month);
        view.setFullYear(year);
        setDates();
        setMonthYear();
        setActive();
    });

    $("div").on('click', "div[class^='day']",function(){
        active.setDate($(this).text());
        active.setMonth(month);
        active.setFullYear(year);
        $('.logdate').val(getDate());
    });

});
