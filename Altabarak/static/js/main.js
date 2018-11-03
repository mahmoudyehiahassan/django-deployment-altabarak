$(function () {
	// body...
	'use strict';
	winH = $(window).height();
	navH = $('.navbar').innerheight();
	$('.slider').height(winH - navH);
})