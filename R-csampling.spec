%global packname  csampling
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.2.1
Release:          1%{?dist}
Summary:          Functions for Conditional Simulation in Regression-Scale Models

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.2-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-marg R-statmod R-survival 


BuildRequires:    R-devel tex(latex) R-marg R-statmod R-survival



%description
Monte Carlo conditional inference for the parameters of a linear nonnormal
regression model

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
%doc %{rlibdir}/csampling/DESCRIPTION
%doc %{rlibdir}/csampling/html
%doc %{rlibdir}/csampling/LICENCE
%doc %{rlibdir}/csampling/CITATION
%{rlibdir}/csampling/R
%{rlibdir}/csampling/INDEX
%{rlibdir}/csampling/help
%{rlibdir}/csampling/csamplingdemo.R
%{rlibdir}/csampling/NAMESPACE
RPM build errors:
%{rlibdir}/csampling/Meta

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.1-1
- initial package for Fedora