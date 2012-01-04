%global packname  shape
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.3.4
Release:          1%{?dist}
Summary:          Functions for plotting graphical shapes, colors

Group:            Applications/Engineering 
License:          GPL (>= 3)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-stats 

BuildRequires:    R-devel tex(latex) R-stats 

%description
Functions for plotting graphical shapes such as ellipses, circles,
cylinders, arrows, ... Support for the book "A practical guide to
ecological modelling - using R as a simulation platform" by Karline
Soetaert and Peter M.J. Herman (2009).  Springer. Includes

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
%doc %{rlibdir}/shape/html
%doc %{rlibdir}/shape/DESCRIPTION
%doc %{rlibdir}/shape/doc
%{rlibdir}/shape/help
%{rlibdir}/shape/INDEX
%{rlibdir}/shape/Meta
%{rlibdir}/shape/demo
%{rlibdir}/shape/R
%{rlibdir}/shape/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.3.4-1
- initial package for Fedora