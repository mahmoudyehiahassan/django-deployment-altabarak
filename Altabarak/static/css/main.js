$(function () {
	// body...
	'use strict';
	var winH = $(window).height();
		navH = $('.navbar').innerHeight();
	$('.slide').height(winH - navH);
})