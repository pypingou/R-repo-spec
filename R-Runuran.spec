%global packname  Runuran
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.18.0
Release:          1%{?dist}
Summary:          R interface to the UNU.RAN random variate generators

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods 

BuildRequires:    R-devel tex(latex) R-methods 

%description
Interface to the UNU.RAN library for Universal Non-Uniform RANdom variate
generators. Thus it allows to build non-uniform random number generators
from quite arbitrary distributions. In particular, it provides an
algorithm for fast numerical inversion for distribution with given density
function. In addition, the package contains densities, distribution
functions and quantiles from a couple of distributions.

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
%doc %{rlibdir}/Runuran/html
%doc %{rlibdir}/Runuran/doc
%doc %{rlibdir}/Runuran/NEWS
%doc %{rlibdir}/Runuran/DESCRIPTION
%{rlibdir}/Runuran/INDEX
%{rlibdir}/Runuran/NAMESPACE
%{rlibdir}/Runuran/help
%{rlibdir}/Runuran/R
RPM build errors:
%{rlibdir}/Runuran/Meta
%{rlibdir}/Runuran/libs

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.18.0-1
- initial package for Fedora