%global packname  ExPD2D
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.1
Release:          1%{?dist}
Summary:          Exact Computation of Bivariate Projection Depth Based on Fortran Code

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Projection depth is one of favorite data depth among all its competitors.
But like all depth functions, compute data depth is a very challenging
problem. This package computes exact projection depth based on FORTRAN
code, but now one can utilize the package in R to get the exact projection
depth of data points.

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
%doc %{rlibdir}/ExPD2D/DESCRIPTION
%doc %{rlibdir}/ExPD2D/html
%{rlibdir}/ExPD2D/NAMESPACE
%{rlibdir}/ExPD2D/libs
%{rlibdir}/ExPD2D/data
%{rlibdir}/ExPD2D/Meta
%{rlibdir}/ExPD2D/R
%{rlibdir}/ExPD2D/INDEX
%{rlibdir}/ExPD2D/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.1-1
- initial package for Fedora