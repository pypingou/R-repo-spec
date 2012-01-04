%global packname  EstCRM
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.1
Release:          1%{?dist}
Summary:          Calibrating Parameters for the Samejima's Continuous IRT Model

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-Hmisc R-lattice 

BuildRequires:    R-devel tex(latex) R-Hmisc R-lattice 

%description
This package includes the tools to estimate item and person parameters for
the Samejima's Continuous Response Model (CRM) via Marginal Maximum
Likelihood and EM algorithm, to compute item fit residual statistics, to
draw empirical 3D item category response curves, to draw theoretical 3D
item category response curves, and to generate data under the CRM for
simulation studies.

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
%doc %{rlibdir}/EstCRM/html
%doc %{rlibdir}/EstCRM/DESCRIPTION
%{rlibdir}/EstCRM/Meta
%{rlibdir}/EstCRM/NAMESPACE
%{rlibdir}/EstCRM/R
%{rlibdir}/EstCRM/help
%{rlibdir}/EstCRM/INDEX
%{rlibdir}/EstCRM/data

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1-1
- initial package for Fedora