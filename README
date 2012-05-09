PyMel is required for this script to work.

The selected node can be of any type as long as it has a outColor attribute.

By default gamma will be corrected by 0.455 0.455 0.455. This can be changed in the script on line 3.
The default Naming convention is {name of the selected node}_GammaCorrect. Also can be changed in the script.

If the outColor attribute is already connected the gamma correct node will be created in between them.

	file.outColor -> blinn.color
	
	Will become 
	
	file.outColor -> gammaCorrect.value    gammaCorrect.outValue -> blinn.color
	

	
If the outColor is not connected the gamma correct node will be created and left dangling.

	file.outColor
	
	Will become 
	
	file.outColor -> gammaCorrect.value
	

Careful if you select a material and run the script it will create a gamma correct node in between the shader and the shading group. It might cause problems.