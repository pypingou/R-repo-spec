%global packname  pensim
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.1.3
Release:          1%{?dist}
Summary:          Simulation of high-dimensional data and parallelized repeated penalized regression

Group:            Applications/Engineering 
License:          GPL (> 2.0)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-MASS R-snow R-rlecuyer R-penalized R-survival 

BuildRequires:    R-devel tex(latex) R-MASS R-snow R-rlecuyer R-penalized R-survival 

%description
Simulation of continuous, correlated high-dimensional data with time to
event or binary response, and parallelized functions for Lasso, Ridge, and
Elastic Net penalized regression with repeated starts and two-dimensional
tuning of the Elastic Net.

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
%doc %{rlibdir}/pensim/DESCRIPTION
%doc %{rlibdir}/pensim/html
%{rlibdir}/pensim/Meta
%{rlibdir}/pensim/INDEX
%{rlibdir}/pensim/help
%{rlibdir}/pensim/data
%{rlibdir}/pensim/R

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.3-1
- initial package for Fedora