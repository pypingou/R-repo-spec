%global packname  alphashape3d
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.2
Release:          1%{?dist}
Summary:          Implementation of the 3D alpha-shape for the reconstruction of 3D sets from a point cloud

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-geometry R-rgl 


BuildRequires:    R-devel tex(latex) R-geometry R-rgl



%description
The package alphashape3d presents the implementation in R of the
alpha-shape of a finite set of points in the three-dimensional space. This
geometric structure generalizes the convex hull and allows to recover the
shape of non-convex and even non-connected sets in 3D, given a random
sample of points taken into it. Besides the computation of the
alpha-shape, the package alphashape3d provides users with functions to
compute the volume of the alpha-shape, identify the connected components
and facilitate the three-dimensional graphical visualization of the
estimated set.

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
%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2-1
- initial package for Fedora