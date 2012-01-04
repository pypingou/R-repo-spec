%global packname  mnormt
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.4.3
Release:          1%{?dist}
Summary:          The multivariate normal and t distributions

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.4-3.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
This package provides functions for computing the density and the
distribution function of multivariate normal and multivariate "t"
variates, and for generating random vectors sampled from these
distributions. Probabilities are computed via a non-Monte Carlo method;
different routines are used for the case d=1, d=2, d>2, if d denotes the
number of dimensions.

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
%doc %{rlibdir}/mnormt/DESCRIPTION
%doc %{rlibdir}/mnormt/html
%{rlibdir}/mnormt/NAMESPACE
%{rlibdir}/mnormt/R
%{rlibdir}/mnormt/INDEX
%{rlibdir}/mnormt/help
%{rlibdir}/mnormt/libs
%{rlibdir}/mnormt/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.4.3-1
- initial package for Fedora