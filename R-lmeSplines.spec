%global packname  lmeSplines
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.4
Release:          1%{?dist}
Summary:          lmeSplines

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-4.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-nlme 

BuildRequires:    R-devel tex(latex) R-nlme 

%description
Add smoothing spline modelling capability to nlme. Fit smoothing spline
terms in Gaussian linear and nonlinear mixed-effects models

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
%doc %{rlibdir}/lmeSplines/doc
%doc %{rlibdir}/lmeSplines/DESCRIPTION
%doc %{rlibdir}/lmeSplines/html
%{rlibdir}/lmeSplines/R
%{rlibdir}/lmeSplines/INDEX
%{rlibdir}/lmeSplines/data
%{rlibdir}/lmeSplines/NAMESPACE
%{rlibdir}/lmeSplines/Meta
%{rlibdir}/lmeSplines/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.4-1
- initial package for Fedora