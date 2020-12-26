$(document).ready(function() {
	var headerHeight = $(".main-header").outerHeight()-52;
	$(window).scroll(function() {
			if (($(".main-menu").length > 0)) {
				if(($(this).scrollTop() > headerHeight)) {
					$(".main-menu").addClass('fixed-top');
				} else {
					$(".main-menu").removeClass('fixed-top');
				}
			}
	});
     function toggleChevron(e) { //this function used in accorion of utregnew
        $(e.target)
            .prev('.panel-heading')
            .find('.indicator')
            .toggleClass('fa-plus fa-minus');
    }
    $('.accordion').on('hidden.bs.collapse', toggleChevron);
    $('.accordion').on('shown.bs.collapse', toggleChevron);
});
