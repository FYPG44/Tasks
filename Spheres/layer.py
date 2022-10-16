from Spheres.point import Point
from Spheres.sphere import Sphere


class Layer(Sphere):
    def generate(self, x0=0, y0=0, z0=0):
        self.__basic_sphere_algorithm(x0, y0, z0)


        
    def __basic_sphere_algorithm(self, x0, y0, z0):
        R = self.radius
        for z in range(R+1):
            Rmin = self.__Give_min(z, R)
            print(f'Rmin: {Rmin}')
            Rmax = self.__Give_max(z, R)
            print(f'Rmax: {Rmax}')
            cstmax = R*R + R - z*z
            print(f'cstmax: {cstmax}')
            cstmin = cstmax - 2*R
            print(f'cstmin: {cstmin}')
            for Rcurr in range(Rmin, Rmax+1):
                self.__circle_sphere(Rcurr, cstmin, cstmax, z)
            # end for
        # end for
        print("Done")
    # end algo

    def __Give_min(self, z, R):
        rmin = R
        global Arcmin
        Arcmin = R*R - R
        mins = Arcmin - z*z
        if (mins < 0): rmin = 0
        else:
            while (mins < Arcmin):
                rmin = rmin - 1
                Arcmin = Arcmin - 2*rmin
            # end while
        # end-if
        return rmin
        # end function

    def __Give_max(self, z, R):
        rmax = R
        Arcmax = R*R - R
        maxs = Arcmax + 2*R - z*z
        while (maxs < Arcmax):
            rmax = rmax - 1
            Arcmax = Arcmax - 2*rmax
        return rmax

    def __circle_sphere(self, Rcurrent, cstmin, cstmax, z):
        R = self.radius
        print(f'Inside circle_sphere')
        x = 0
        print(f'x : {x}')
        y = Rcurrent
        print(f'y : {y}')
        delta = Rcurrent
        print(f'delta: {delta}')
        cst_local_min = Rcurrent*Rcurrent + R - cstmax
        print(f'cst_local_min: {cst_local_min}')
        cst_local_max = Rcurrent*Rcurrent + R - cstmin
        print(f'cst_local_max: {cst_local_max}')
        while y >= x:
            print(f'x:{x}, y: {y}, z:{z}, delta: {delta}, clmin: {cst_local_min}, clmax: {cst_local_max}')
            if delta >= cst_local_min and delta < cst_local_max:
                pt = Point(x = x, y = y, z = z)
                self.points.extend(pt.plot_48_voxels())
            if delta > 2*x:
                delta = delta - 2*x - 1
                x = x + 1
            elif (delta <= 2*(R-y)):
                delta = delta + 2*y - 1
                y = y - 1
            else:
                delta = delta + 2*(y-x-1)
                x = x + 1
                y = y - 1


    

        


    

    