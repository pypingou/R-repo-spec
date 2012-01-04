%global packname  AdMit
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.01.03.1
Release:          1%{?dist}
Summary:          Adaptive Mixture of Student-t distributions

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1-01.03.1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-mvtnorm 

BuildRequires:    R-devel tex(latex) R-mvtnorm 

%description
This package provides functions to perform the fitting of an adaptive
mixture of Student-t distributions to a target density through its kernel
function. The mixture approximation can then be used as the importance
density in importance sampling or as the candidate density in the
Metropolis-Hastings algorithm to obtain quantities of interest for the
target density itself.

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
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.01.03.1-1
- initial package for Fedora