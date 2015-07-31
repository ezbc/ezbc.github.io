---
layout: post
title: Rocking Chair
author:
category: woodworking
comments: true
tags: 
---


In 2012 I adopted
[plans](https://books.google.com/books?id=388DAAAAMBAJ&pg=PA112#v=onepage&q&f=false)
for an Art & Crafts Rocking Chair from Popular Mechanics for a tech theater
woodworking project. I redrafted the plans on paper:

<img id="zoom_03" src="/images/2015-07-27/rocking_chair_plans_small.png" style="width:100%" data-zoom-image="/images/2015-07-27/rocking_chair_plans_large.png"/>

<script>
    $('#zoom_01').elevateZoom({zoomWindowPosition: 6});
</script>

<script>
    $("#zoom_03").elevateZoom({constrainType:"height", constrainSize:274, zoomType: "lens", containLensZoom: true, cursor: 'pointer', }); //pass the images to Fancybox 

</script>


Below are images of chair itself.

<div class="variable-width">
  <div> <img src="/images/2015-07-27/rocking_chair_01_small.jpg"/> </div>
  <div> <img src="/images/2015-07-27/rocking_chair_02_small.jpg"/> </div>
  <div> <img src="/images/2015-07-27/rocking_chair_03_small.jpg"/> </div>
</div>

<style>
    .slick-prev:before, .slick-next:before { 
        color:blue !important;
    }
    .slider {margin: 10%;}
.variable-width {
    width: 90%;
    margin: auto;
}
</style>

<script>
$('.autoplay').slick({
  slidesToShow: 2,
  slidesToScroll: 1,
  autoplay: true,
  autoplaySpeed: 2000,
});
$('.variable-width').slick({
  dots: true,
  infinite: true,
  speed: 300,
  slidesToShow: 1,
  centerMode: true,
  variableWidth: true
});
$('.fade').slick({
  dots: true,
  infinite: true,
  speed: 500,
  fade: true,
  cssEase: 'linear'
});
</script>





