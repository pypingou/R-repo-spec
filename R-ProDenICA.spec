%global packname  ProDenICA
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Product Density Estimation for ICA using tilted Gaussian density estimates

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-gam 

BuildRequires:    R-devel tex(latex) R-gam 

%description
A direct and flexible method for estimating an ICA model. This approach
estimates the densities for each component directly via a tilted gaussian.
The tilt functions are estimated via a GAM poisson model. Details can be
found in "Elements of Statistical Learning (2nd Edition)" Section 14.7.4

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
%doc %{rlibdir}/ProDenICA/html
%doc %{rlibdir}/ProDenICA/DESCRIPTION
%{rlibdir}/ProDenICA/Meta
%{rlibdir}/ProDenICA/NAMESPACE
%{rlibdir}/ProDenICA/help
%{rlibdir}/ProDenICA/INDEX
%{rlibdir}/ProDenICA/R

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora