%global packname  geometry
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.2.0
Release:          1%{?dist}
Summary:          Mesh generation and surface tesselation

Group:            Applications/Engineering 
License:          GPL (>= 2) + file LICENSE
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.2-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
This package makes the qhull library (www.qhull.org) available in R, in a
similar manner as in Octave and MATLAB. Qhull computes convex hulls,
Delaunay triangulations, halfspace intersections about a point, Voronoi
diagrams, furthest-site Delaunay triangulations, and furthest-site Voronoi
diagrams. It runs in 2-d, 3-d, 4-d, and higher dimensions. It implements
the Quickhull algorithm for computing the convex hull. Qhull does not
support constrained Delaunay triangulations, or mesh generation of
non-convex objects, but the package does include some R functions that
allow for this. Currently the package only gives access to Delaunay
triangulation and convex hull computation.

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%doc %{rlibdir}/geometry/NEWS
%doc %{rlibdir}/geometry/html
%doc %{rlibdir}/geometry/DESCRIPTION
%doc %{rlibdir}/geometry/doc
%{rlibdir}/geometry/NAMESPACE
%{rlibdir}/geometry/Meta
%{rlibdir}/geometry/R
%{rlibdir}/geometry/LICENSE
%{rlibdir}/geometry/INDEX
%{rlibdir}/geometry/help
%{rlibdir}/geometry/libs

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2.0-1
- initial package for Fedora