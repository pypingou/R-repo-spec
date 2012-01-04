%global packname  growthrate
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.1
Release:          1%{?dist}
Summary:          Bayesian reconstruction of growth velocity

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-Matrix R-clime R-mvtnorm 

BuildRequires:    R-devel tex(latex) R-Matrix R-clime R-mvtnorm 

%description
A nonparametric empirical Bayes method for recovering gradients (or growth
velocities) from observations of smooth functions (e.g., growth curves) at
isolated time points.

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
%doc %{rlibdir}/growthrate/html
%doc %{rlibdir}/growthrate/DESCRIPTION
%{rlibdir}/growthrate/help
%{rlibdir}/growthrate/Meta
%{rlibdir}/growthrate/LICENSE
%{rlibdir}/growthrate/data
%{rlibdir}/growthrate/R
%{rlibdir}/growthrate/INDEX
%{rlibdir}/growthrate/NAMESPACE

%changelog
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1-1
- initial package for Fedora