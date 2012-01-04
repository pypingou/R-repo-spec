%global packname  alphahull
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.2.1
Release:          1%{?dist}
Summary:          Generalization of the convex hull of a sample of points in the plane

Group:            Applications/Engineering 
License:          file LICENSE
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.2-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-tripack R-sgeostat R-splancs 

BuildRequires:    R-devel tex(latex) R-tripack R-sgeostat R-splancs 

%description
This package computes the alpha-shape and alpha-convex hull of a given
sample of points in the plane. The concepts of alpha-shape and
alpha-convex hull generalize the definition of the convex hull of a finite
set of points. The programming is based on the duality between the Voronoi
diagram and Delaunay triangulation. The package also includes a function
that returns the Delaunay mesh of a given sample of points and its dual
Voronoi diagram in one single object.

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
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2.1-1
- initial package for Fedora