%global packname  gmvalid
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.22
Release:          1%{?dist}
Summary:          Validation of graphical models

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-grid R-CoCo R-epitools 

BuildRequires:    R-devel tex(latex) R-grid R-CoCo R-epitools 

%description
Simulate data sets given a dependence model, validate graphical models
using the bootstrap, find the best prediction model using cross

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
%doc %{rlibdir}/gmvalid/DESCRIPTION
%doc %{rlibdir}/gmvalid/html
%{rlibdir}/gmvalid/help
%{rlibdir}/gmvalid/CITATION.R
%{rlibdir}/gmvalid/INDEX
%{rlibdir}/gmvalid/Meta
%{rlibdir}/gmvalid/R
%{rlibdir}/gmvalid/data

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.22-1
- initial package for Fedora