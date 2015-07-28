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

<div align="center">

  <img id="zoom_02"
      src="/images/2015-07-27/rocking_chair_01_small.jpg"
      data-zoom-image="/images/2015-07-27/rocking_chair_01_large.jpg"/>

  <div id="gal1">

    <a href="#" data-image="/images/2015-07-27/rocking_chair_01_small.jpg"
      data-zoom-image="/images/2015-07-27/rocking_chair_01_large.jpg">
      <img id="img_01" src="/images/2015-07-27/rocking_chair_01_thumb.jpg"/>
    </a>

    <a href="#" data-image="/images/2015-07-27/rocking_chair_02_small.jpg"
      data-zoom-image="/images/2015-07-27/rocking_chair_02_large.jpg">
      <img id="img_01" src="/images/2015-07-27/rocking_chair_02_thumb.jpg"/>
    </a>

    <a href="#" data-image="/images/2015-07-27/rocking_chair_03_small.jpg"
      data-zoom-image="/images/2015-07-27/rocking_chair_03_large.jpg">
      <img id="img_01" src="/images/2015-07-27/rocking_chair_03_thumb.jpg"/>
    </a>

  </div>
</div>


<script>
    $("#zoom_02").elevateZoom({constrainType:"height", constrainSize:400, zoomType: "lens", containLensZoom: true, gallery:'gal1', cursor: 'pointer', galleryActiveClass: "active"}); //pass the images to Fancybox 
    
    $("#zoom_02").bind("click", function(e) {
        var ez = $('#zoom_02').data('elevateZoom'); 
            $.fancybox(ez.getGalleryList());
        return false; });

</script>
<style>
/*set a border on the images to prevent shifting*/ 
    #gal1 img{border:2px solid white;} /*Change the colour*/ 
    .active img{border:2px solid #333 !important;} 
</style>






