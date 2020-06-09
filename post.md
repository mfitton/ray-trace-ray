# Parallel Ray Tracing Made Simple
Results
____________________Parallelized, no optimization ______________________

NO CHUNKING 871.21s user 226.71s system 210% cpu 8:40.77 total
CHUNK_SIZE = 100 34.22s user 6.78s system 42% cpu 1:37.15 total

    ________________Unparallelized, no optimization ______________________
python raytracing.py  177.35s user 0.73s system 99% cpu 2:58.81 total


## Key Definitions
*Ray Tracing* is a method of generating computer images by imitating the way that a camera captures photographs. However, while a physical camera takes in light to capture an image of its surroundings, a ray tracer operates the process in reverse. It sends rays out from its “camera,” through a 2d plane whose coordinates correspond to pixels in an image. These rays then  may intersect with and reflect off of objects in the scene. The color intensities of these pixels are partially determined by the angle of the reflection compared to the light source, When a ray reflects from an object and travels directly towards a light source, the pixel corresponding to that ray will be more affected by that light.  You can imagine reversing the trajectory of the ray that you have traced, and you would end up with a ray going from the light source to the camera. It happens that tracing feasible paths from the camera to to light sources is more performant than tracing light rays from each light source to the camera, as most such light rays miss.

*Ray*is a python framework developed by the RISELab at  UC Berkeley with the goal of making it is easy to scale programs. Even if you’re just using your laptop, Ray can help you scale a workload to leverage all of your cores in parallel. Python has a global interpreter lock, so typically for running code in parallel you need to reach for running multiple processes, which do not share memory. This leads to a programmer having to keep the constraints of the multiprocessing library in mind—not so with Ray. Ray lets you further scale your code to run across multiple machines.
