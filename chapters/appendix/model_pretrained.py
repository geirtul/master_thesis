Model: "sequential_1"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
block1_conv1 (Conv2D)        (None, 16, 16, 64)        1792      
_________________________________________________________________
block1_conv2 (Conv2D)        (None, 16, 16, 64)        36928     
_________________________________________________________________
block1_pool (MaxPooling2D)   (None, 8, 8, 64)          0         
_________________________________________________________________
block2_conv1 (Conv2D)        (None, 8, 8, 128)         73856     
_________________________________________________________________
block2_conv2 (Conv2D)        (None, 8, 8, 128)         147584    
_________________________________________________________________
block2_pool (MaxPooling2D)   (None, 4, 4, 128)         0         
_________________________________________________________________
block3_conv1 (Conv2D)        (None, 4, 4, 256)         295168    
_________________________________________________________________
block3_conv2 (Conv2D)        (None, 4, 4, 256)         590080    
_________________________________________________________________
block3_conv3 (Conv2D)        (None, 4, 4, 256)         590080    
_________________________________________________________________
block3_pool (MaxPooling2D)   (None, 2, 2, 256)         0         
_________________________________________________________________
block4_conv1 (Conv2D)        (None, 2, 2, 512)         1180160   
_________________________________________________________________
block4_conv2 (Conv2D)        (None, 2, 2, 512)         2359808   
_________________________________________________________________
block4_conv3 (Conv2D)        (None, 2, 2, 512)         2359808   
_________________________________________________________________
block4_pool (MaxPooling2D)   (None, 1, 1, 512)         0         
_________________________________________________________________
block5_conv1 (Conv2D)        (None, 1, 1, 512)         2359808   
_________________________________________________________________
block5_conv2 (Conv2D)        (None, 1, 1, 512)         2359808   
_________________________________________________________________
block5_conv3 (Conv2D)        (None, 1, 1, 512)         2359808   
_________________________________________________________________
flatten_1 (Flatten)          (None, 512)               0         
_________________________________________________________________
dense (Dense)                (None, 10)                5130      
_________________________________________________________________
dense_1 (Dense)              (None, 1)                 11        
=================================================================
Total params: 14,719,829
Trainable params: 14,719,829
Non-trainable params: 0
